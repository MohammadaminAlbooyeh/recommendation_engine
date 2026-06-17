import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
from typing import Optional


def compute_cosine_similarity(matrix: np.ndarray, dense_output: bool = True):
    from sklearn.metrics.pairwise import cosine_similarity as cos_sim
    return cos_sim(matrix, dense_output=dense_output)


def compute_pearson_correlation(matrix: np.ndarray):
    return np.corrcoef(matrix)


def compute_jaccard_similarity(matrix: csr_matrix) -> np.ndarray:
    binary = (matrix > 0).astype(float)
    intersection = binary.dot(binary.T)
    row_sums = binary.sum(axis=1).A1
    union = row_sums[:, np.newaxis] + row_sims[np.newaxis, :] - intersection
    union = np.maximum(union, 1e-10)
    return intersection / union


def compute_euclidean_similarity(matrix: np.ndarray) -> np.ndarray:
    from sklearn.metrics.pairwise import euclidean_distances
    distances = euclidean_distances(matrix)
    return 1.0 / (1.0 + distances)
