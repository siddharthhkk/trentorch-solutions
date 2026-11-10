import numpy as np


def gram_schmidt(vectors):
    """
    vectors: a list of 1D NumPy arrays, all the same length, guaranteed
             linearly independent

    Returns:
        A list of the same length: an orthonormal basis (unit length,
        mutually perpendicular) spanning the same space, built by
        processing vectors in the given order.
    """
    # TODO: Implement Gram-Schmidt from Theory: for each vector, subtract
    # its projection onto every already-built basis vector, then
    # normalize what's left.
    basis = []
    for v in vectors:
        ortho = np.copy(v).astype(float)
        for u in basis:
            ortho -= np.dot(v, u) * u
        basis.append(ortho / np.linalg.norm(ortho))
    return basis
    pass
