def multiply(n):
    if n == 0:
        return 0;
    if n > 0:
        return n * (5 ** len(str(n)))
    else:
        return n * (5 ** len(str(abs(n))))