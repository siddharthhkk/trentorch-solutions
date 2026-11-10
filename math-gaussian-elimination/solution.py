import numpy as np


def gaussian_eliminate(A, b):
    """
    A: a square (n, n) NumPy array that does not require row swaps
    b: a length-n NumPy array

    Returns:
        (U, c): U is A row-reduced to upper-triangular form, c is b
        transformed by the same row operations, such that Ux = c has
        the same solution as Ax = b.
    """
    # TODO: Implement elimination on copies of A and b in lockstep,
    # from Theory.
    U = A.astype(float).copy()
    c = b.astype(float).copy()

    for i in range(len(c)):
        for j in range(i + 1, len(c)):
            factor = U[j, i] / U[i, i]
            U[j, i:] -= factor * U[i, i:]
            c[j] -= factor * c[i]
    return U, c
    pass


def back_substitute(U, c):
    """
    U: an upper-triangular (n, n) NumPy array
    c: a length-n NumPy array

    Returns:
        x, the solution to Ux = c, solved from the last row up.
    """
    # TODO: Implement back substitution from Theory's formula.
    x = np.zeros(len(c))
    for i in range(len(c) - 1, -1, -1):
        dotp = np.dot(U[i, i + 1:], x[i + 1:])
        x[i] = (c[i] - dotp) / U[i, i]
    return x
    pass
