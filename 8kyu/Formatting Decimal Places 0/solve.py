def two_decimal_places(n):
    return float("{0:.2f}".format(n))


def two_decimal_places(n):
    return float("%.2f" % n)


def two_decimal_places(n):
    return round(n, 2)



two_decimal_places = lambda n : round(n,2)


two_decimal_places = __import__("functools").partial(round, ndigits=2)
