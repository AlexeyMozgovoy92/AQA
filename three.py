import math


def factorial(b):
    if b == 0:
        return 1
    else:
        return b * factorial(b - 1)

def absolute(b):
    if b < 0:
        c = b * (-1)
        return c
    else:
        return b

def procent(b, b1):
    a=(b1 / b) * 100
    return a

def power(b, b1):
    m = 1
    for _ in range(b1):
        m = m * b
    return b

def logarithm(b, b1):
    return math.log(b1, b)

