from codecs import encode

def rot13(message):
    return encode(message, "rot13")
    
    
 
# No cheating solution   
# I didn't see the last sentence lol

def rot13(message):
    return message.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"))