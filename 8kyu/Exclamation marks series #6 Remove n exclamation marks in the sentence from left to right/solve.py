def remove(st, n):
    # you can set how many times you want to replace, by adding one more argument!
    return st.replace("!", "", n)


remove=lambda s,n:s.replace('!','',n)


def remove(s, n):
    return ''.join(s.split('!', n))

def remove(s, n):
    while n > 0:
        s = s.replace('!','',1)
        n -= 1
    return s