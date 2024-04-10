def sorter(textbooks):
    return sorted(textbooks, key=str.casefold)


def sorter(textbooks):
    return sorted(textbooks, key=lambda tb: tb.upper())


def sorter(textbooks):
    return sorted(textbooks,key=str.lower)


def sorter(textbooks):
    return sorted(textbooks, key = lambda arg: arg.lower())


sorter = lambda x: sorted(x,key=lambda s:s.lower())
