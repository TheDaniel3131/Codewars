def count_me(data):
    if not data.isdigit():
        return ""
    else:
        output = ""
        i = 0
        while i < len(data):
            count = 1
            while i + 1 < len(data) and data[i] == data[i+1]:
                i += 1
                count += 1
            output += str(count) + data[i]
            i += 1
        return output

    
from itertools import groupby


def count_me(data):
    result = []
    for i, j in groupby(data):
        if i.isdigit():
            result.append(f'{len(list(j))}{i}')
        else:
            return ''
    return ''.join(result)


from itertools import groupby

def count_me(data):
    return ''.join(f'{len(list(g))}{c}' for c, g in groupby(data)) if data.isdigit() else ''