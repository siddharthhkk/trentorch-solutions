def adamw_decay_split(theta: float, u: float, eta: float, lam: float) -> float:
    """
    theta: current parameter value.
    u: Adam's already-computed adaptive update (no decay folded in).
    eta: learning rate.
    lam: weight-decay coefficient.

    theta' = theta - eta * u - eta * lam * theta

    Returns the updated theta.
    """
    # TODO: apply the adaptive step and the decoupled decay step as two
    # separate terms.
    return theta - eta * u - eta * lam * theta
    pass
