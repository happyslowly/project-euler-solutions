import sys
import math


def perf(func):
    import timeit, inspect
    def decorated(*args, **kwargs):
        start = timeit.default_timer() * 1000
        result = func(*args, **kwargs)
        end = timeit.default_timer() * 1000
        print("%s(%s) took %dms to complete" % (
            func.__name__,
            ','.join([str(x) for x in args]),
            int(round(end - start))))
        return result
    return decorated


def verify(a, b, msg=None):
    try:
        assert a == b
    except AssertionError:
        if msg: print(msg, file=sys.stderr)
        print("AssertionError, expected: %s, actual: %s" % (str(a), str(b)), file=sys.stderr)


def is_prime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0: return False
    return True


def get_factors(n):
    factors = []
    for x in range(2, int(math.sqrt(n)) + 1):
        while n % x == 0:
            factors.append(x)
            n = int(n / x)
    if n > 1: factors.append(n)
    return factors


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
