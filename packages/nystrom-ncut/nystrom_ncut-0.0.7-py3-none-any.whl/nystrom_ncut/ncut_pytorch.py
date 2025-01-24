import logging
from typing import Literal, Tuple

import torch
import torch.nn.functional as Fn

from .common import (
    DistanceOptions,
    SampleOptions,
)
from .nystrom import (
    EigSolverOptions,
    OnlineKernel,
    OnlineNystrom,
    solve_eig,
)
from .propagation_utils import (
    affinity_from_features,
    run_subgraph_sampling,
)


class LaplacianKernel(OnlineKernel):
    def __init__(
        self,
        affinity_focal_gamma: float,
        distance: DistanceOptions,
        eig_solver: EigSolverOptions,
    ):
        self.affinity_focal_gamma = affinity_focal_gamma
        self.distance: DistanceOptions = distance
        self.eig_solver: EigSolverOptions = eig_solver

        # Anchor matrices
        self.anchor_features: torch.Tensor = None               # [n x d]
        self.A: torch.Tensor = None                             # [n x n]
        self.Ainv: torch.Tensor = None                          # [n x n]

        # Updated matrices
        self.a_r: torch.Tensor = None                           # [n]
        self.b_r: torch.Tensor = None                           # [n]

    def fit(self, features: torch.Tensor) -> None:
        self.anchor_features = features                         # [n x d]
        self.A = affinity_from_features(
            self.anchor_features,                               # [n x d]
            affinity_focal_gamma=self.affinity_focal_gamma,
            distance=self.distance,
        )                                                       # [n x n]
        d = features.shape[-1]
        U, L = solve_eig(
            self.A,
            num_eig=d + 1,  # d * (d + 3) // 2 + 1,
            eig_solver=self.eig_solver,
        )                                                       # [n x (d + 1)], [d + 1]
        self.Ainv = U @ torch.diag(1 / L) @ U.mT                # [n x n]
        self.a_r = torch.sum(self.A, dim=-1)                    # [n]
        self.b_r = torch.zeros_like(self.a_r)                   # [n]

    def update(self, features: torch.Tensor) -> torch.Tensor:
        B = affinity_from_features(
            self.anchor_features,                               # [n x d]
            features,                                           # [m x d]
            affinity_focal_gamma=self.affinity_focal_gamma,
            distance=self.distance,
        )                                                       # [n x m]
        b_r = torch.sum(B, dim=-1)                              # [n]
        b_c = torch.sum(B, dim=-2)                              # [m]
        self.b_r = self.b_r + b_r                               # [n]

        rowscale = self.a_r + self.b_r                          # [n]
        colscale = b_c + B.mT @ self.Ainv @ self.b_r            # [m]
        scale = (rowscale[:, None] * colscale) ** -0.5          # [n x m]
        return (B * scale).mT                                   # [m x n]

    def transform(self, features: torch.Tensor = None) -> torch.Tensor:
        rowscale = self.a_r + self.b_r                          # [n]
        if features is None:
            B = self.A                                          # [n x n]
            colscale = rowscale                                 # [n]
        else:
            B = affinity_from_features(
                self.anchor_features,                           # [n x d]
                features,                                       # [m x d]
                affinity_focal_gamma=self.affinity_focal_gamma,
                distance=self.distance,
            )                                                   # [n x m]
            b_c = torch.sum(B, dim=-2)                          # [m]
            colscale = b_c + B.mT @ self.Ainv @ self.b_r        # [m]
        scale = (rowscale[:, None] * colscale) ** -0.5          # [n x m]
        return (B * scale).mT                                   # [m x n]


class NCUT(OnlineNystrom):
    """Nystrom Normalized Cut for large scale graph."""

    def __init__(
        self,
        n_components: int = 100,
        affinity_focal_gamma: float = 1.0,
        num_sample: int = 10000,
        sample_method: SampleOptions = "farthest",
        distance: DistanceOptions = "cosine",
        eig_solver: EigSolverOptions = "svd_lowrank",
        normalize_features: bool = None,
        chunk_size: int = 8192,
    ):
        """
        Args:
            n_components (int): number of top eigenvectors to return
            affinity_focal_gamma (float): affinity matrix temperature, lower t reduce the not-so-connected edge weights,
                smaller t result in more sharp eigenvectors.
            num_sample (int): number of samples for Nystrom-like approximation,
                reduce only if memory is not enough, increase for better approximation
            sample_method (str): subgraph sampling, ['farthest', 'random'].
                farthest point sampling is recommended for better Nystrom-approximation accuracy
            distance (str): distance metric for affinity matrix, ['cosine', 'euclidean', 'rbf'].
            eig_solver (str): eigen decompose solver, ['svd_lowrank', 'lobpcg', 'svd', 'eigh'].
            normalize_features (bool): normalize input features before computing affinity matrix,
                default 'None' is True for cosine distance, False for euclidean distance and rbf
            chunk_size (int): chunk size for large-scale matrix multiplication
        """
        OnlineNystrom.__init__(
            self,
            n_components=n_components,
            kernel=LaplacianKernel(affinity_focal_gamma, distance, eig_solver),
            eig_solver=eig_solver,
            chunk_size=chunk_size,
        )
        self.num_sample: int = num_sample
        self.sample_method: SampleOptions = sample_method
        self.anchor_indices: torch.Tensor = None
        self.distance: DistanceOptions = distance
        self.normalize_features: bool = normalize_features
        if self.normalize_features is None:
            if distance in ["cosine"]:
                self.normalize_features = True
            if distance in ["euclidean", "rbf"]:
                self.normalize_features = False

        self.chunk_size: int = chunk_size

    def _fit_helper(
        self,
        features: torch.Tensor,
        precomputed_sampled_indices: torch.Tensor,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        _n = features.shape[0]
        if self.num_sample >= _n:
            logging.info(
                f"NCUT nystrom num_sample is larger than number of input samples, nyström approximation is not needed, setting num_sample={_n}"
            )
            self.num_sample = _n

        assert self.distance in ["cosine", "euclidean", "rbf"], "distance should be 'cosine', 'euclidean', 'rbf'"

        if self.normalize_features:
            # features need to be normalized for affinity matrix computation (cosine distance)
            features = torch.nn.functional.normalize(features, dim=-1)

        if precomputed_sampled_indices is not None:
            _sampled_indices = precomputed_sampled_indices
        else:
            _sampled_indices = run_subgraph_sampling(
                features,
                self.num_sample,
                sample_method=self.sample_method,
            )
        self.anchor_indices = torch.sort(_sampled_indices).values
        sampled_features = features[self.anchor_indices]
        OnlineNystrom.fit(self, sampled_features)

        _n_not_sampled = _n - len(sampled_features)
        if _n_not_sampled > 0:
            unsampled_indices = torch.full((_n,), True, device=features.device).scatter_(0, self.anchor_indices, False)
            unsampled_features = features[unsampled_indices]
            V_unsampled, _ = OnlineNystrom.update(self, unsampled_features)
        else:
            unsampled_indices = V_unsampled = None
        return unsampled_indices, V_unsampled

    def fit(
        self,
        features: torch.Tensor,
        precomputed_sampled_indices: torch.Tensor = None,
    ):
        """Fit Nystrom Normalized Cut on the input features.
        Args:
            features (torch.Tensor): input features, shape (n_samples, n_features)
            precomputed_sampled_indices (torch.Tensor): precomputed sampled indices, shape (num_sample,)
                override the sample_method, if not None
        Returns:
            (NCUT): self
        """
        NCUT._fit_helper(self, features, precomputed_sampled_indices)
        return self

    def fit_transform(
        self,
        features: torch.Tensor,
        precomputed_sampled_indices: torch.Tensor = None,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Args:
            features (torch.Tensor): input features, shape (n_samples, n_features)
            precomputed_sampled_indices (torch.Tensor): precomputed sampled indices, shape (num_sample,)
                override the sample_method, if not None

        Returns:
            (torch.Tensor): eigen_vectors, shape (n_samples, num_eig)
            (torch.Tensor): eigen_values, sorted in descending order, shape (num_eig,)
        """
        unsampled_indices, V_unsampled = NCUT._fit_helper(self, features, precomputed_sampled_indices)
        V_sampled, L = OnlineNystrom.transform(self)

        if unsampled_indices is not None:
            V = torch.zeros((len(unsampled_indices), self.n_components), device=features.device)
            V[~unsampled_indices] = V_sampled
            V[unsampled_indices] = V_unsampled
        else:
            V = V_sampled
        return V, L


def axis_align(eigen_vectors: torch.Tensor, max_iter=300):
    """Multiclass Spectral Clustering, SX Yu, J Shi, 2003

    Args:
        eigen_vectors (torch.Tensor): continuous eigenvectors from NCUT, shape (n, k)
        max_iter (int, optional): Maximum number of iterations.

    Returns:
        torch.Tensor: Discretized eigenvectors, shape (n, k), each row is a one-hot vector.
    """
    # Normalize eigenvectors
    n, k = eigen_vectors.shape
    eigen_vectors = Fn.normalize(eigen_vectors, p=2, dim=-1)

    # Initialize R matrix with the first column from a random row of EigenVectors
    R = torch.empty((k, k), device=eigen_vectors.device)
    R[0] = eigen_vectors[torch.randint(0, n, (1,))].squeeze()

    # Loop to populate R with k orthogonal directions
    c = torch.zeros(n, device=eigen_vectors.device)
    for i in range(1, k):
        c += torch.abs(eigen_vectors @ R[i - 1])
        R[i] = eigen_vectors[torch.argmin(c, dim=0)]

    # Iterative optimization loop
    eps = torch.finfo(torch.float32).eps
    prev_objective = torch.inf
    for _ in range(max_iter):
        # Discretize the projected eigenvectors
        idx = torch.argmax(eigen_vectors @ R.mT, dim=-1)
        M = torch.zeros((k, k)).index_add_(0, idx, eigen_vectors)

        # Compute the NCut value
        objective = torch.norm(M)

        # Check for convergence
        if torch.abs(objective - prev_objective) < eps:
            break
        prev_objective = objective

        # SVD decomposition
        U, S, Vh = torch.linalg.svd(M, full_matrices=False)
        R = U @ Vh

    return Fn.one_hot(idx, num_classes=k).to(torch.float), R
