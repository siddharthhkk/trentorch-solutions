import numpy as np


def householder_vector(x):
    """
    x: 1D array of floats

    Returns:
        A 1D array v of the same length such that the reflection across
        the plane perpendicular to v sends x to
        [-sign(x[0]) * norm(x), 0, ..., 0], with sign(0) = 1. Returns the
        zero vector when x is the zero vector. x must not be modified.
    """
    # TODO: Implement the direction from Theory, with the sign chosen to
    # avoid cancellation in the first entry.
    norm_x = np.linalg.norm(x)
    if np.isclose(norm_x, 0.0):
        return np.zeros_like(x, dtype=float)
    v = x.copy().astype(float)
    s = -1.0 if v[0] < 0 else 1.0
    v[0] += s * norm_x
    return v
    pass


def householder_matrix(v):
    """
    v: 1D array of floats, the mirror direction

    Returns:
        The n x n matrix I - 2 v v^T / (v^T v). Returns the identity when
        v is the zero vector.
    """
    # TODO: Implement the formula from Theory.
    v_norm_sq = np.dot(v, v)
    if np.isclose(v_norm_sq, 0.0):
        return np.eye(len(v), dtype=float)
    return np.eye(len(v)) - (2.0 / v_norm_sq) * np.outer(v, v)
    pass


def apply_householder(v, a):
    """
    v: 1D array of floats, the mirror direction
    a: 1D vector or 2D matrix with len(v) rows

    Returns:
        The reflection of a (each column, for a matrix) with the same
        shape as a, computed without building the n x n matrix. Returns a
        copy of a when v is the zero vector. v and a must not be modified.
    """
    # TODO: Implement a - 2 v (v^T a) / (v^T v) from Theory.
    v_norm_sq = np.dot(v, v)
    if np.isclose(v_norm_sq, 0.0):
        return a.copy().astype(float)
    if a.ndim == 1:
        # Vector case: v^T a is a scalar
        v_dot_a = np.dot(v, a)
        return a - (2.0 / v_norm_sq) * v_dot_a * v
    else:
        # Matrix case: v^T a is a 1D array of dot products for each column
        v_dot_a = np.dot(v, a)  # Shape: (cols,)
        # Reshape v to (rows, 1) and v_dot_a to (1, cols) to use broadcasting
        return a - (2.0 / v_norm_sq) * v[:, np.newaxis] * v_dot_a[np.newaxis, :]
    pass
