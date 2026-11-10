import numpy as np

from _load import load_solution

householder_vector = load_solution("math-householder-reflections").householder_vector
apply_householder = load_solution("math-householder-reflections").apply_householder


def householder_qr(a):
    """
    a: m x n float array with m >= n

    Returns:
        (Q, R): Q is m x m and orthogonal, R is m x n with exact zeros
        below the diagonal, and Q @ R equals a. Uses one Householder
        mirror per column; skips a column whose mirror direction is zero.
        a must not be modified.
    """
    # TODO: Clear each column below the diagonal with a mirror, as in Theory,
    # and accumulate the mirrors into Q.
    m, n = a.shape
    R = np.array(a, dtype=float)
    Q = np.eye(m, dtype=float)
    
    k_max = min(m, n)
    for j in range(k_max):
        x = R[j:, j]
        v = householder_vector(x)
        if v is None or np.all(v == 0): continue
            
        R[j:, j:] = apply_householder(v, R[j:, j:])
        Q[:, j:] = apply_householder(v, Q[:, j:].T).T
    R[np.tril_indices(m, -1, n)] = 0.0
    return Q, R
    pass


def back_substitution(r, y):
    """
    r: n x n upper-triangular float array with a nonzero diagonal
    y: 1D float array of length n

    Returns:
        The 1D array x with r @ x == y, found from the last row upward
        with a loop (do not call np.linalg.solve).
    """
    # TODO: Solve from the last row upward, as in Theory.
    n = r.shape[0]
    x = np.zeros_like(y, dtype=float)
    x_copy = np.array(y, dtype=float)

    for i in range(n - 1, -1, -1):
        x[i] = (x_copy[i] - np.dot(r[i, i + 1 :], x[i + 1 :])) / r[i, i]
    return x
    pass


def least_squares_qr(a, b):
    """
    a: m x n float array with full column rank, m >= n
    b: 1D float array of length m

    Returns:
        The 1D array x of length n minimising the squared error of
        a @ x - b, using householder_qr and back_substitution. Do not form
        a.T @ a.
    """
    # TODO: Reduce to the triangular system from Theory.
    Q, R = householder_qr(a)
    c = Q.T @ b
    n = a.shape[1]
    R_top = R[:n, :]
    c_top = c[:n]
    x = back_substitution(R_top, c_top)
    return x
    pass
