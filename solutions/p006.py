#!/usr/bin/env python
from solutions.helpers import verify, perf


@perf
def p006_naive(n):
    return (sum(range(1, n + 1)) * sum(range(1, n + 1))
            - sum([x * x for x in range(1, n + 1)]))

verify(2640, p006_naive(10))
verify(25164150, p006_naive(100))

