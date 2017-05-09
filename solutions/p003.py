#!/usr/bin/env python
from solutions.helpers import get_factors, is_prime, verify


def p003(n):
    return max([x for x in get_factors(n) if is_prime(x)])

verify(29, p003(13195))
verify(6857, p003(600851475143))