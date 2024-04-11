def remainder(a, b):
    if min(a, b) == 0:
        return None;
    return max(a,b) % min(a, b)


def remainder(a:int, b:int)->int:
    '''Returns remainder of the larger of two numbers 
    being divided by the smaller of two numbers.
    Returns None for divide by zero.'''
    try:
        return max(a, b) % min(a, b)
    except ZeroDivisionError:
        return None

    
def remainder(a,b):
    if a < b:
        a, b = (b, a)
    if b == 0:
        return None 
    return a % b 