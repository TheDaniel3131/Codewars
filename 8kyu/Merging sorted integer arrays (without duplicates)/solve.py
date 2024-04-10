from collections import Counter


def merge_arrays(first, second): 
    c_arr = Counter(first + second)
    xf_c_arr = [*c_arr]
    return sorted(xf_c_arr)



def merge_arrays(a, b): 
    return sorted(set(a + b))


def merge_arrays(first, second): 
    return sorted(set(first + second))


def merge_arrays(*a):
    result = []
    for sublist in a:
        for element in sublist:
            if not (element in result):
                result.append(element)
    return sorted(result)