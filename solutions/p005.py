#!/usr/bin/env python
from functools import reduce

from solutions.helpers import get_factors, verify, perf


@perf
def p005_naive(n):
    factors = get_factors(n)
    for x in range(n-1, 0, -1):
        f = get_factors(x)
        for i in factors:
            if i in f:
                f.remove(i)
        factors.extend(f)
    return reduce(lambda x, y: x * y, factors)

verify(2520, p005_naive(10))
verify(232792560, p005_naive(20))