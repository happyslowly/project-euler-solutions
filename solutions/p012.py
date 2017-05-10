#!/usr/bin/env python
import math

from solutions.helpers import verify, perf


@perf
def p012_naive(n):
    if n == 1: return 1
    b = 2
    while True:
        b += 1
        triangle = sum(range(1, b))
        count = 0
        for i in range(1, int(math.sqrt(triangle)) + 1):
            if triangle % i == 0: count += 2
        if count >= n: return triangle


verify(28, p012_naive(5))
verify(76576500, p012_naive(500))
