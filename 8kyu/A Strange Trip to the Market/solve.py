def is_loch_ness_monster(string):
    ln_phrases = ["tree fiddy", "three fifty", "3.50"]

    if string == "":
        return False;
    else:
        for i in ln_phrases:
            if i in string:
                return True;
        return False;
    

def is_lock_ness_monster(s):
    return any(i in s for i in ('tree fiddy', 'three fifty', '3.50'))


import re

def is_lock_ness_monster(s):
    return bool(re.search(r"3\.50|tree fiddy|three fifty", s))