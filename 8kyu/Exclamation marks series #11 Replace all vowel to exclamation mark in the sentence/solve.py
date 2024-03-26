def replace_exclamation(st):
    new_st = ""
    for i in st:
        if i in 'aeiouAEIOU':
            new_st += "!"
        else:
            new_st += i
    return new_st
        
    
def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)


import re


def replace_exclamation(s):
    return re.sub('[aeiouAEIOU]', '!', s)


def replace_exclamation(s):
    return s.translate(str.maketrans('aeiouAEIOU', '!' * 10))