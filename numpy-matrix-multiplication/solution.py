import numpy as np


def matmul_from_scratch(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compute the matrix product of 2D arrays `a` (shape (m, n))
    and `b` (shape (n, p)), implementing the definition directly
    with explicit loops over i, j, and k — do NOT use @, matmul,
    or dot here. Return the resulting (m, p) array.
    This exists to build the definition into your understanding
    before using NumPy's built-in version below.
    """
    m, n = a.shape
    n_b, p = b.shape
    if n != n_b:
        raise ValueError("Inner dimensions must match for matrix multiplication.")
    result = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i, j] += a[i, k] * b[k, j]   
    return result
    pass


def matmul_builtin(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Compute the same result as matmul_from_scratch, using the @
    operator.
    """
    return a @ b
    pass


def compare_matmul_and_elementwise(a: np.ndarray, b: np.ndarray) -> dict:
    """
    Given two square matrices of the same shape, compute both
    a @ b and a * b.

    Return a dictionary:
      {
        "matmul_result": a @ b,
        "elementwise_result": a * b,
        "results_are_different": <True unless the two results
            happen to be identical, checked with array
            comparison, not assumed>
      }
    """
    matmul_res = a @ b
    elementwise_res = a * b
    results_are_different = not np.array_equal(matmul_res, elementwise_res)
    return {'matmul_result': matmul_res,
        'elementwise_result': elementwise_res,
        'results_are_different': results_are_different
    }
    pass
