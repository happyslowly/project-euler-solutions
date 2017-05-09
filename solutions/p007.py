#!/usr/bin/env python
from solutions.helpers import is_prime, verify, perf


@perf
def p007_naive(n):
    if n == 1:
        return 2
    p, i = 3, 1
    while True:
        if is_prime(p):
            i += 1
            if i == n:
                return p
        p += 2


verify(13, p007_naive(6))
verify(104743, p007_naive(10001))
