def disemvowel(string_):
    vowels = "AEIOUaeiou"
    new_string = ""
    for i in string_:
        if i not in vowels:
            new_string += i

    return new_string


def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")