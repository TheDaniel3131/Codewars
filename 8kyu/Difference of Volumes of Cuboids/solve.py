def find_difference(a, b):
    return abs((a[0] * a[1] * a[2]) - (b[0] * b[1] * b[2]))


from numpy import prod

def find_difference(a, b):
    return abs(prod(a) - prod(b))


def find_difference(a, b):
    A = B = 1
    for i, j in zip(a, b):
        A *= i
        B *= j
    return abs(A - B)


from operator import mul
from functools import reduce
def find_difference(a, b):
    return abs(reduce(mul, a) - reduce(mul, b))


find_difference = lambda (a, b, c), (x, y, z): abs(a * b * c - x * y * z)
