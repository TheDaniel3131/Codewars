def how_much_i_love_you(nb_petals):
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]

    if nb_petals == None and nb_petals <= 0:
        return None;
    else:
        return phrases[(nb_petals - 1) % 6];
