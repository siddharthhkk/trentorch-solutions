import numpy as np


def mgf(values, probabilities, t):
    """
    values: 1D array-like of the outcomes X can take
    probabilities: 1D array-like, same length, non-negative, sums to 1
    t: float or NumPy array

    Returns:
        The moment generating function E[exp(t * X)] at t, with the same
        shape as t.
    """
    # TODO: Implement the weighted sum from Theory.
    values = np.asarray(values)
    probabilities = np.asarray(probabilities)
    t_arr = np.asarray(t)
    exp_tx = np.exp(np.expand_dims(t_arr, axis=-1) * values)
    
    return np.sum(exp_tx * probabilities, axis=-1)
    pass


def pgf(probabilities, z):
    """
    probabilities: 1D array-like where probabilities[k] = P(X = k)
    z: float or NumPy array

    Returns:
        The probability generating function E[z ** X] at z, with the same
        shape as z.
    """
    # TODO: Implement the series from Theory with the probabilities as
    # coefficients.
    probabilities = np.asarray(probabilities)
    z_arr = np.asarray(z)
    ks = np.arange(len(probabilities))
    z_to_k = np.power(np.expand_dims(z_arr, axis=-1), ks)
    
    return np.sum(z_to_k * probabilities, axis=-1)
    pass


def mgf_moments(mgf_fn, step=1e-3):
    """
    mgf_fn: function taking a float t and returning a float M(t)
    step: the finite-difference step h

    Returns:
        (first_moment, second_moment) as floats: M'(0) and M''(0),
        estimated with central finite differences of size `step`.
    """
    # TODO: Differentiate numerically at t = 0, as in Theory.
    h = step
    first_moment = (mgf_fn(h) - mgf_fn(-h)) / (2 * h)
    second_moment = (mgf_fn(h) - 2 * mgf_fn(0) + mgf_fn(-h)) / (h ** 2)
    
    return float(first_moment), float(second_moment)
    pass


def pgf_mean_variance(probabilities):
    """
    probabilities: 1D array-like where probabilities[k] = P(X = k)

    Returns:
        (mean, variance) as floats, computed from the derivatives of the
        probability generating function at z = 1.
    """
    # TODO: Use G'(1), G''(1) and the variance identity from Theory.
    probabilities = np.asarray(probabilities)
    ks = np.arange(len(probabilities))
    
    g_prime_1 = np.sum(ks * probabilities)
    g_double_prime_1 = np.sum(ks * (ks - 1) * probabilities)
    mean = g_prime_1
    variance = g_double_prime_1 + mean - (mean ** 2)
    
    return float(mean), float(variance)
    pass


def sum_distribution(p, q):
    """
    p, q: probability lists for independent X and Y, where p[k] = P(X = k)
        and q[k] = P(Y = k)

    Returns:
        A 1D array of length len(p) + len(q) - 1 holding P(X + Y = n).
    """
    # TODO: Multiply the two generating functions, as in Theory.
    return np.convolve(p, q)
    pass
