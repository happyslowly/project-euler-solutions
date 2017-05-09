#!/usr/bin/env python
from solutions.helpers import verify


def p001(n):
    return sum([x for x in range(1, n) if x % 3 == 0 or x % 5 == 0])

verify(23, p001(10))
verify(233168, p001(1000))
