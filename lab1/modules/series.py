from decimal import Decimal

series_pow = Decimal(-1.0) / Decimal(3)


def nth_term(n):
    if n < 1:
        raise AttributeError('n should be bigger than zero.')
    return Decimal(n + 6) ** series_pow


def partial_sum(n, polynomial=nth_term):
    if n < 1:
        raise AttributeError('n should be bigger than zero.')
    res = Decimal(0)
    for i in range(1,n + 1):
        next_term = polynomial(i)
        res = res + next_term
    return res