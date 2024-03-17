def fake_bin(x):
    new_x = ""
    for num in x:
        if int(num) < 5:
            new_x += "0"
        else:
            new_x += "1"
    return new_x
    
def fake_bin(x):
    map = str.maketrans('123456789', '000011111')
    return x.translate(map)

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)