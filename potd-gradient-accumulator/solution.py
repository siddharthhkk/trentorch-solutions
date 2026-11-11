import numpy as np
def gradient_accumulator(
    theta: float, eta: float, microbatches: list[tuple[int, float]]
) -> tuple[float, float]:
    """
    microbatches: list of (n_j, g_j) pairs, n_j examples with mean
    gradient g_j.

    g = sum(n_j * g_j) / sum(n_j)   (example-weighted mean, NOT the mean
    of the microbatch means).
    theta' = theta - eta * g.

    Return (g, theta_prime).
    """
    # TODO: weight by example count, divide exactly once.
    n_j, g_j = zip(*microbatches)
    g = np.sum(np.multiply(n_j, g_j)) / np.sum(n_j)
    theta_prime = theta - eta * g
    return g, theta_prime
    pass
