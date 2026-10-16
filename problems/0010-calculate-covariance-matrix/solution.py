import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # np.cov treats rows as variables and columns as observations by default
    cov_matrix = np.cov(vectors)
    return cov_matrix.tolist()