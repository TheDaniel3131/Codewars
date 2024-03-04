from codecs import encode

def rot13(message):
    return encode(message, "rot13")