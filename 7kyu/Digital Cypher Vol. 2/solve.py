def decode(code, key):
    key = str(key)
    alphabet_letters = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for i in range(len(code)):
        idx = (code[i] - int(key[i % len(key)]) - 1) % 26
        letter = alphabet_letters[idx]
        output += letter
    return output



alp = 'abcdefghijklmnopqrstuvwxyz'
def decode(code, key):
    key = (str(key)*len(code))[:len(code)]
    result = ''
    for i,j in zip(code, key):
        result += alp[i-int(j)-1]
    return result