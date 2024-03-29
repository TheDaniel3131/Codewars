def shortcut( s ):
    rm_lower_s = ""
    for i in s:
        if i not in "aeiou":
            rm_lower_s += i
    return rm_lower_s


def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')


def shortcut( s ):
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s


import re

def shortcut( s ):
    return re.sub('[aoeui]', '', s)


def shortcut(s):
    return s.translate(s.maketrans('', '', 'aeiou'))


def shortcut(s):
    for i in ["a","e","i","o","u"]:
        if i in s:
            s = s.replace(i,"")

    return(s)