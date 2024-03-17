def fake_bin(x):
    new_x = ""
    for num in x:
        if int(num) < 5:
            new_x += "0"
        else:
            new_x += "1"
    return new_x
    