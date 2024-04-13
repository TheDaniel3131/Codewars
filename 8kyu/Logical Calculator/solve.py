def logical_calc(booleans, operator):
    if operator == "AND":
        return all(booleans)
    elif operator == "OR":
        return any(booleans)
    elif operator == "XOR":
        return sum(booleans) % 2 == 1
    else:
        return None
    
    

from functools import reduce

def logical_calc(array, op):
    ops = {
        "AND" : lambda x,y: x & y,
        "OR"  : lambda x,y: x | y,
        "XOR" : lambda x,y: x ^ y
    }
    return reduce(ops[op], array)



def logical_calc(array, op):
    res = array[0]
    for x in array[1:]:
        if op == "AND":
            res &= x
        elif op == "OR":
            res |= x
        else:
            res ^= x
        
    return res #boolean


def logical_calc(array, op):
    result = False
    if len(array) == 1: return array[0]
    
    if op == "AND": result = array[0] and array[1]
    if op == "OR": result = array[0] or array[1]
    if op == "XOR": result = array[0] ^ array[1]
    
    for n in range(2,len(array)):
        if op == "AND":
            result = result and array[n]
        if op == "OR":
            result = result or array[n]
        if op == "XOR":
            result = result ^ array[n]
            
    return result