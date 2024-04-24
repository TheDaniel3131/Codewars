def test(r):
    class_average = round((sum(r) / len(r)), 3)
    dictionary = {
        "h": 0,
        "a": 0,
        "l": 0
    }
    for mark in r:
        if mark in [9, 10]:
            dictionary["h"] += 1
        elif mark in [7, 8]:
            dictionary["a"] += 1
        else:
            dictionary["l"] += 1

    list = [class_average, dictionary]
    if dictionary["a"] == 0 and dictionary["l"] == 0:
        return [class_average, dictionary, "They did well"]
    return list


def test(r):
    d = {'h': 0, 'a': 0, 'l': 0}
    for mark in r:
        if mark >= 9:
            d['h'] += 1
        elif mark >= 7:
            d['a'] += 1
        else:
            d['l'] += 1
    
    if d['a'] + d['l'] == 0:
        return [round(sum(r)/len(r), 3), d, 'They did well']
    else:
        return [round(sum(r)/len(r), 3), 
                
            
                
from collections import Counter
from statistics import mean

def test(marks):
    mark_type_counts = Counter('h' if m >= 9 else 'a' if m >= 7 else 'l' for m in marks)
    mark_type_counts.update({'h': 0, 'a': 0, 'l': 0})
    res = [round(mean(marks), 3), mark_type_counts]
    if mark_type_counts['h'] == len(marks):
        res.append('They did well')
    return res
                
                
from statistics import mean

def test(r):
    dct = {'l': 0, 'a': 0, 'h': 0}
    for n in r: dct[ 'lah'[(n>6) + (n>8)] ] += 1
    return [round(mean(r), 3), dct] + ['They did well'] * (sum(dct.values()) == dct['h'])