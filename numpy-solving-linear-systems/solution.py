import numpy as np


def solve_system(coefficients: np.ndarray, constants: np.ndarray) -> np.ndarray:
    """
    Solve the linear system coefficients @ x = constants for x,
    using np.linalg.solve.
    """
    return np.linalg.solve(coefficients, constants)
    pass


def solve_via_inverse(coefficients: np.ndarray, constants: np.ndarray) -> np.ndarray:
    """
    Solve the same system as solve_system, but by explicitly
    computing the inverse of `coefficients` and multiplying it by
    `constants`. This exists to be compared against solve_system.
    """
    inverse = np.linalg.inv(coefficients)
    return inverse @ constants
    pass


def solutions_agree(coefficients: np.ndarray, constants: np.ndarray) -> bool:
    """
    Solve the system both ways (using solve_system and
    solve_via_inverse) and return True if the two solutions are
    approximately equal (use np.allclose), False otherwise.
    """
    sol1 = solve_system(coefficients, constants)
    sol2 = solve_via_inverse(coefficients, constants)
    return bool(np.allclose(sol1, sol2))
    pass
