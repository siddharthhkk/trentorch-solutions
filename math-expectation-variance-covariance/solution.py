import numpy as np


def expectation(values, probabilities):
    """
    values: 1D array-like, the outcomes a discrete random variable X can take
    probabilities: 1D array-like, P(X = values[i]) for each i

    Returns:
        E[X], as a float, from Theory.
    """
    # TODO: Implement E[X] = sum(x_i * P(x_i)) from Theory.
    values = np.asarray(values, dtype=float)
    probabilities = np.asarray(probabilities, dtype=float)
    return float(np.sum(values*probabilities))
    pass


def variance(values, probabilities):
    """
    values, probabilities: same as `expectation`

    Returns:
        Var(X) = E[(X - E[X])^2], as a float, from Theory.
    """
    # TODO: Implement Var(X) using `expectation`, from Theory.
    values = np.asarray(values, dtype=float)
    probabilities = np.asarray(probabilities, dtype=float)
    return float(np.sum(np.square(values - expectation(values, probabilities)) * probabilities))
    pass


def pmf_covariance(x_values, y_values, joint_probabilities):
    """
    x_values: 1D array-like, the outcomes X can take
    y_values: 1D array-like, the outcomes Y can take
    joint_probabilities: 2D array-like, joint_probabilities[i, j] =
        P(X=x_values[i], Y=y_values[j])

    Returns:
        Cov(X, Y) = E[(X - E[X])(Y - E[Y])], as a float, from Theory.
    """
    # TODO: Implement Cov(X, Y) from Theory, using the joint distribution's
    # own marginals for E[X] and E[Y].
    x_values = np.asarray(x_values, dtype=float)
    y_values = np.asarray(y_values, dtype=float)
    joint_probabilities = np.asarray(joint_probabilities, dtype=float)
    marginal_x = joint_probabilities.sum(axis=1)
    marginal_y = joint_probabilities.sum(axis=0)
    mean_x = expectation(x_values, marginal_x)
    mean_y = expectation(y_values, marginal_y)

    total = 0.0
    for i, x in enumerate(x_values):
        for j, y in enumerate(y_values):
            total += joint_probabilities[i, j] * (x - mean_x) * (y - mean_y)
    return float(total)
    pass


def sample_mean(x: np.ndarray) -> float:
    """
    The sample mean estimates a distribution's expectation E[X]:
    simply the average of the observed values.
    """
    return float(np.mean(x))
    pass


def sample_variance(x: np.ndarray, ddof: int = 0) -> float:
    """
    The sample variance estimates a distribution's Var(X). `ddof`
    ("delta degrees of freedom") controls the divisor: ddof=0 divides
    by n (the biased/population estimator), ddof=1 divides by n-1
    (Bessel's correction, the unbiased estimator). See Theory for why
    the distinction matters.
    """
    return float(np.var(x, ddof=ddof))
    pass


def covariance(x: np.ndarray, y: np.ndarray, ddof: int = 0) -> float:
    """
    Covariance measures whether x and y tend to move together (positive),
    move oppositely (negative), or show no consistent relationship
    (near zero):

        cov(x, y) = (1/(n - ddof)) * sum((x_i - mean(x)) * (y_i - mean(y)))

    Same ddof convention 05-expectation-covariance's sample_variance uses
    (in fact, covariance(x, x, ddof) is exactly sample_variance(x, ddof)).
    """
    n = len(x)
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    return float(np.sum((x - mean_x) * (y - mean_y)) / (n - ddof))
    pass


def correlation(x: np.ndarray, y: np.ndarray) -> float:
    """
    Correlation rescales covariance into a unitless number in [-1, 1],
    by dividing out each variable's own spread:

        corr(x, y) = cov(x, y) / (std(x) * std(y))
    """
    return float(covariance(x, y) / (np.std(x) * np.std(y)))
    pass
