#!!/usr/bin/env python
from solutions.helpers import verify, perf


@perf
def p009_naive(n):
    for a in range(1, n // 3 + 1):
        for b in range(a + 1, (n - a) // 2 + 1):
            c = n - a - b
            if a * a + b * b == c * c:
                return a * b * c


verify(31875000, p009_naive(1000))
