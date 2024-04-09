def well(x):
    count = x.count("good")
    if 1 <= count <= 2:
        return "Publish!"
    elif count > 2:
        return "I smell a series!"
    else:
        return "Fail!"
    
    
def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'


def well(x):
    if 'good' in x:
        return 'I smell a series!' if x.count('good') > 2 else 'Publish!'
    else:
        return 'Fail!'