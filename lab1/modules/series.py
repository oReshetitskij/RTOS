from decimal import Decimal

series_pow = Decimal(-1.0) / Decimal(3)


def nth_term(n):
    """
    Calculates nth term of (x + 6) ^ (-1/3) harmonic series.

    :param n: Term number in series
    :return: Nth term of series

    >>> nth_term(1)
    Decimal('0.5227579585747102167482961872')
    """
    if n < 1:
        raise AttributeError('n should be bigger than zero.')
    return Decimal(n + 6) ** series_pow


def partial_sum(n, series=nth_term):
    """
    Calculates partial sum for given series.

    :param n: Count of terms for sum
    :param series: Function to express series
    :return: Partial sum of series

    >>> partial_sum(3, lambda x: x ** 2)
    Decimal('14')
    """
    if n < 1:
        raise AttributeError('n should be bigger than zero.')
    res = Decimal(0)
    for i in range(1,n + 1):
        next_term = series(i)
        res = res + next_term
    return res