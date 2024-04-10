def flip(d, a):
    if d == 'R':
        return sorted(a[::-1])
    else:
        return sorted(a, reverse=True)
    
    
def flip(d,a):
    return sorted(a, reverse=d=='L')


def flip(d, a):
    if d == 'L':
        return sorted(a, reverse=True)
    else:
        return sorted(a)
    
    
def flip(d, a):
    if d == 'L':
        a.sort(reverse=True)
    elif d == 'R':
        a.sort()
    return a
    # Do some magic