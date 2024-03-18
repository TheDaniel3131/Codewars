def count_sheep(n):
    sheepo = ""
    if n == 0:
        return ''
    for i in range(1, n+1):
        sheepo += f"{i} sheep..."
    return sheepo


def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))