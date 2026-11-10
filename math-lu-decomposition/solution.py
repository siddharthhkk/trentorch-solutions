import numpy as np


def lu_decompose(A):
    """
    A: a square (n, n) NumPy array that does not require row swaps
       (every pivot encountered during elimination is non-zero)

    Returns:
        (L, U): L is lower-triangular with 1s on the diagonal, U is
        upper-triangular, such that L @ U reconstructs A exactly.
    """
    # TODO: Implement Gaussian elimination on a copy of A (building U),
    # recording each elimination multiplier into L, from Theory.
    n = A.shape[0]
    U = A.astype(float).copy()
    L = np.eye(n, dtype=float)

    for i in range(n):
        for j in range(i+1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]
    return L, U
    pass
