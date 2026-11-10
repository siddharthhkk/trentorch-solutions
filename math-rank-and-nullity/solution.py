import numpy as np


def rank(A):
    """
    A: an (m, n) NumPy array

    Returns:
        The rank of A: the number of linearly independent rows,
        computed via row-reduction (skip a column with no usable pivot
        rather than treating it as an error).
    """
    # TODO: Implement row-reduction with a separate pivot-row/pivot-
    # column pointer, counting pivots found, from Theory.
    A = np.array(A, dtype=float)
    m, n = A.shape
    r = 0
    c = 0
    while r < m and c < n:
        pivot = r + np.argmax(np.abs(A[r:, c]))
        if np.abs(A[pivot, c]) < 1e-12:
            c += 1
            continue
        if pivot != r:
            A[[r, pivot]] = A[[pivot, r]]

        for i in range(r + 1, m):
            factor = A[i, c] / A[r, c]
            A[i, c:] -= factor * A[r, c:]
        r += 1
        c += 1
    return r
    pass


def nullity(A):
    """
    A: an (m, n) NumPy array

    Returns:
        The nullity of A: A.shape[1] - rank(A), per the Rank-Nullity
        Theorem.
    """
    # TODO: Implement using rank(A) from Theory's formula.
    A = np.array(A, dtype=float)
    return A.shape[1] - rank(A)
    pass
