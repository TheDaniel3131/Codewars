def neutralise(s1, s2):
    result = ''
    for i, j in zip(s1, s2):
        if i == j:
            result += i or j
        else:
            result += "0"
    return result