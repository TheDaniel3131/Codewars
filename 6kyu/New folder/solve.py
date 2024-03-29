def spin_words(sentence):
    res = ""
    for word in sentence.split():
        if len(word) > 4:
            res += " " + word[::-1]
        else:
            res += " " + word
    return res.lstrip()


def spin_words(sentence):
    return " ".join([w[::-1] if len(w) >= 5 else w for w in sentence.split()])


def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string
    