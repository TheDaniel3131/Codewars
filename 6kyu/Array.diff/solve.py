def array_diff(a, b):
    return [x for x in a if x not in b]


def array_diff(a, b):
    return [x for x in a if x not in set(b)]


def array_diff(a, b):
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a


def array_diff(a, b):
    for n in b:
        while(n in a):
            a.remove(n)
    return a