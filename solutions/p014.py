#!/usr/bin/env python
from solutions.helpers import perf, verify


cache = {1: [1]}


def next_number(n):
    return n >> 1 if n & 1 == 0 else 3 * n + 1


def seq(start):
    path = []
    while start not in cache:
        path.append(start)
        start = next_number(start)
    path.extend(cache[start])
    cache[path[0]] = path
    return path


@perf
def p014_naive(bound):
    max_path, max_n = 0, 0
    for x in range(1, bound):
        if len(seq(x)) > max_path:
            max_path = len(seq(x))
            max_n = x
    return max_n


verify(10, len(seq(13)))
verify(837799, p014_naive(10**6))
