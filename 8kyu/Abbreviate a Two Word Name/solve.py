def abbrev_name(name):
    first_name = name.split(' ')[0]
    last_name = name.split(' ')[-1]
    
    # print(first_name)
    # print(last_name)

    return (first_name[0] + "." + last_name[0]).upper()
    
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
    
 
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]
    
def abbrevName(name):
    names = name.split()
    return f"{names[0][0]}.{names[1][0]}".upper()2