#!/usr/bin/env python
from solutions.helpers import verify, perf


def fibonacci(n):
    numbers = []
    a, b = 0, 1
    while True:
        t = a + b
        a = b
        b = t
        if b >= n: break
        numbers.append(b)
    return numbers


@perf
def p002_naive(n):
    return sum([x for x in fibonacci(n) if x % 2 == 0])


verify(4613732, p002_naive(4000000))
