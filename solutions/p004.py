#!/usr/bin/env python
import math

from solutions.helpers import is_palindrome, verify


def p004(n):
    low, high = int(math.pow(10, n - 1)), int(math.pow(10, n))
    return max([i * j for i in range(low, high) for j in range(low, high) if is_palindrome(i * j)])

verify(9009, p004(2))
verify(906609, p004(3))