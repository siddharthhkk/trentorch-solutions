def geometric_partial_sum(a, r, n):
    """
    a: first term (float)
    r: common ratio (float)
    n: how many terms to add (int, n >= 0)

    Returns:
        The sum of the first n terms of a + a*r + a*r**2 + ..., as a
        float, in constant time (no loop over the terms). Handles r == 1.
    """
    # TODO: Implement the closed form from Theory.
    if n <= 0: return 0.0
    if r == 1.0: return float(a * n)
    return float(a * (1 - r ** n) / (1.0 - r))
    pass


def geometric_series_sum(a, r):
    """
    a: first term, r: common ratio

    Returns:
        The sum of the infinite series, as a float.

    Raises:
        ValueError: if abs(r) >= 1, because the series has no finite sum.
    """
    # TODO: Implement the infinite-sum formula from Theory.
    if abs(r) >= 1.0:
        raise ValueError('Series diverges because abs(r) >= 1')
    return float(a / (1.0 - r))
    pass


def terms_needed(a, r, tolerance):
    """
    a: first term, r: common ratio with abs(r) < 1, tolerance: float > 0

    Returns:
        The smallest integer n >= 0 such that the infinite sum minus the
        sum of the first n terms is smaller than tolerance in absolute
        value. Returns 0 when a == 0.

    Raises:
        ValueError: if abs(r) >= 1 or tolerance <= 0.
    """
    # TODO: Solve the tail inequality from Theory for n.
    if abs(r) >= 1.0:
        raise ValueError("The series diverges because abs(r) >= 1.")
    if tolerance <= 0.0:
        raise ValueError("Tolerance must be strictly positive.")
    if a == 0.0: 
        return 0
    if r == 0.0:
        return 1 if abs(a) >= tolerance else 0

    target = (tolerance * abs(1.0 - r)) / abs(a)
    if target >= 1.0: 
        return 0
        
    n_float = math.log(target) / math.log(abs(r))
    n = math.floor(n_float) + 1
    
    while abs(a) * (abs(r) ** n) >= tolerance * abs(1.0 - r): 
        n += 1
    while n > 0 and abs(a) * (abs(r) ** (n - 1)) < tolerance * abs(1.0 - r): 
        n -= 1

    return max(0, n)
    pass
