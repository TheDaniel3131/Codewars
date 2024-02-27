def is_uppercase(inp):
    special_chars = "!@#$%^&*()_+{}|:'',./<>?[]\-="
    if inp.isupper() or all(char in special_chars for char in inp):
        return True
    else:
        return False