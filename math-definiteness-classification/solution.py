import numpy as np


def leading_principal_minors(a: np.ndarray) -> np.ndarray:
    """
    a: n x n array

    Returns:
        A 1D array of length n whose entry k - 1 is the determinant of
        the top-left k x k block of a.
    """
    # TODO: Take the determinant of each growing top-left block.
    n = a.shape[0]
    minors = np.zeros(n)
    
    for k in range(1, n + 1):
        block = a[:k, :k]
        minors[k - 1] = np.linalg.det(block)
    return minors
    pass


def is_positive_definite_sylvester(a: np.ndarray) -> bool:
    """
    a: a 2D array

    Returns:
        True if a is square, symmetric (np.allclose) and every leading
        principal minor is strictly positive, otherwise False. Do not
        compute eigenvalues.
    """
    # TODO: Apply Sylvester's criterion from Theory.
    if a.ndim != 2 or a.shape[0] != a.shape[1]: return False
    if not np.allclose(a, a.T): return False
    minors = leading_principal_minors(a)
    return np.all(minors > 0)
    pass


def classify_definiteness(a: np.ndarray, tol: float = 1e-10) -> str:
    """
    a: a square, symmetric 2D array
    tol: eigenvalues within tol of zero count as zero

    Returns:
        One of "positive definite", "positive semidefinite",
        "negative definite", "negative semidefinite", "indefinite" or
        "zero" ("zero" only when every eigenvalue is within tol of zero).

    Raises:
        ValueError: if a is not square or not symmetric (np.allclose).
    """
    # TODO: Classify by the signs of the eigenvalues, as in Theory.
    if a.ndim != 2 or a.shape[0] != a.shape[1]:
        raise ValueError("Matrix must be 2D and square.")
        
    if not np.allclose(a, a.T):
        raise ValueError("Matrix must be symmetric.")
    eigenvalues = np.linalg.eigh(a)[0]
    
    is_zero = np.abs(eigenvalues) <= tol
    is_pos = eigenvalues > tol
    is_neg = eigenvalues < -tol
    
    if np.all(is_zero):return "zero"
    elif np.all(is_pos): return "positive definite"
    elif np.all(is_neg): return "negative definite"
    elif np.any(is_pos) and np.any(is_neg): return "indefinite"
    elif np.any(is_pos) and np.any(is_zero): return "positive semidefinite"
    else: return "negative semidefinite"
    pass


def critical_point_type(hessian: np.ndarray, tol: float = 1e-10) -> str:
    """
    hessian: the Hessian at a point where the gradient is zero

    Returns:
        "local minimum" (positive definite), "local maximum" (negative
        definite), "saddle point" (indefinite) or "inconclusive"
        (semidefinite or zero).

    Raises:
        ValueError: if the Hessian is not square and symmetric.
    """
    # TODO: Map the class from classify_definiteness to a verdict.
    definiteness = classify_definiteness(hessian, tol=tol)
    mapping = {
        "positive definite": "local minimum",
        "negative definite": "local maximum",
        "indefinite": "saddle point",
        "positive semidefinite": "inconclusive",
        "negative semidefinite": "inconclusive",
        "zero": "inconclusive"
    }
    return mapping[definiteness]
    pass
