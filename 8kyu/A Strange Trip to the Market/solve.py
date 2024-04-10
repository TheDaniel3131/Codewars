def is_loch_ness_monster(string):
    ln_phrases = ["tree fiddy", "three fifty", "3.50"]

    if string == "":
        return False;
    else:
        for i in ln_phrases:
            if i in string:
                return True;
        return False;