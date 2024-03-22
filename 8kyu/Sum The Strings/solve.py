def sum_str(a, b):
    if not a and not b:
        return "0" 
    else:
        ab = int(a or "0") + int(b or "0")
        return str(ab)

