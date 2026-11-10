import numpy as np


def is_positive_semidefinite(a: np.ndarray, tol: float = 1e-10) -> bool:
    """
    a: a 2D array
    tol: eigenvalues down to -tol count as zero

    Returns:
        True if a is square, symmetric (np.allclose) and has no
        eigenvalue below -tol, otherwise False.
    """
    # TODO: Loosen the strict eigenvalue test from 01-positive-definite.
    if a.ndim != 2 or a.shape[0] != a.shape[1]: return False
    if not np.allclose(a, a.T):
        return False
    eigenval = np.linalg.eigvalsh(a)
    return bool(np.all(eigenval >= -tol))
    pass


def gram_matrix(x: np.ndarray) -> np.ndarray:
    """
    x: m x d array whose rows are vectors

    Returns:
        The m x m matrix of all pairwise dot products of the rows of x.
    """
    # TODO: Build the Gram matrix from Theory.
    return np.dot(x, x.T)
    pass


def nearest_psd(a: np.ndarray) -> np.ndarray:
    """
    a: a square 2D array

    Returns:
        The symmetric positive semi-definite matrix closest to
        (a + a.T) / 2 in Frobenius norm, same shape as a. a must not be
        modified.
    """
    # TODO: Clip the negative eigenvalues of the symmetric part, as in Theory.
    b = (a + a.T) / 2
    s, u = np.linalg.eigh(b)

    s_clipped = np.maximum(s, 0)
    return (u * s_clipped) @ u.T
    pass
