#!/usr/bin/env python
from solutions.helpers import is_prime, perf, verify


@perf
def p010_naive(n):
    if n < 2: return 0
    if n == 2: return 2
    return 2 + sum([i for i in range(3, n + 1, 2) if is_prime(i)])

verify(17, p010_naive(10))
verify(142913828922, p010_naive(2000000))
