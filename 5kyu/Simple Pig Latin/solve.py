def pig_it(text):
    word = text.split(' ')
    sentence = ''
    
    for i in word:
        if i.isalpha():
            sentence += i[1:] + i[0] + "ay "
        else:
            sentence += i[1:] + i[0] + " "
    return sentence.rstrip()