def to_alternating_case(s):
    return s.swapcase()


to_alternating_case = str.swapcase


def to_alternating_case(string):
    return ''.join(string[i].upper() if string[i].islower() else string[i].lower() for i in range(len(string)))