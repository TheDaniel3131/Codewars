def abbrev_name(name):
    first_name = name.split(' ')[0]
    last_name = name.split(' ')[-1]
    
    # print(first_name)
    # print(last_name)

    return (first_name[0] + "." + last_name[0]).upper()