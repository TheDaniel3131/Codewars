def correct(s):
    dict = {
        "5": "S",
        "0": "O",
        "1": "I"
    }
    
    return "".join([dict.get(i, i) for i in s])


def correct(string):
    return string.translate(str.maketrans("501", "SOI"))