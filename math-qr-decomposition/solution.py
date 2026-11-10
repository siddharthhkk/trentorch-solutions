import numpy as np


def qr_decompose(A):
    """
    A: an (m, n) NumPy array with linearly independent columns

    Returns:
        (Q, R): Q is (m, n) with orthonormal columns, R is (n, n)
        upper-triangular, such that Q @ R reconstructs A exactly.
    """
    # TODO: Implement Gram-Schmidt column by column, recording each
    # projection coefficient into R and each leftover norm into R's
    # diagonal, from Theory.
    A = np.asarray(A, dtype=float)
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    V = A.copy()
    
    for i in range(n):
        R[i, i] = np.linalg.norm(V[:, i])
        Q[:, i] = V[:, i] / R[i, i]

        for j in range(i + 1, n):
            R[i, j] = Q[:, i] @ V[:, j]
            V[:, j] -= R[i, j] * Q[:, i]
    return Q, R
    pass
