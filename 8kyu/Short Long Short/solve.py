def solution(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a

    
    
def solution(a, b):
    return '{0}{1}{0}'.format(*sorted((a, b), key=len))



def solution(a, b):
    short, long = sorted((a, b), key=len)
    return short + long + short



    def solution(a, b):
    if len(a) > len(b):
        return f'{b}{a}{b}'
    else:
        return f'{a}{b}{a}'