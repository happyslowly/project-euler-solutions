#!/usr/bin/env python
from solutions.helpers import get_factors, is_prime, verify, perf


@perf
def p003_naive(n):
    return max([x for x in get_factors(n) if is_prime(x)])

verify(29, p003_naive(13195))
verify(6857, p003_naive(600851475143))