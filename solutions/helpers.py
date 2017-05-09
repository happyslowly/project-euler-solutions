import sys
import math

def verify(a, b, msg=None):
    try:
        assert a == b
    except AssertionError:
        if msg: print(msg, file=sys.stderr)
        print("AssertionError, expected: %s, actual: %s" % (str(a), str(b)), file=sys.stderr)


def is_prime(n):
    for x in range(2, int(math.sqrt(n)) + 1):
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
