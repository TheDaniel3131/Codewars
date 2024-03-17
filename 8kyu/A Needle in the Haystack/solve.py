def find_needle(haystack):
    sentence = "found the needle at position "
    if "needle" in haystack:
        return sentence + str(haystack.index("needle"))