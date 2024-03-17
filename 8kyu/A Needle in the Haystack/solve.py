def find_needle(haystack):
    sentence = "found the needle at position "
    if "needle" in haystack:
        return sentence + str(haystack.index("needle"))
    
    
def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'