def correct(s):
    dict = {
        "5": "S",
        "0": "O",
        "1": "I"
    }
    
    return "".join([dict.get(i, i) for i in s])
