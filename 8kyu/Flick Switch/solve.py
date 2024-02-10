def flick_switch(lst):
    result = []
    switch = True  
    for i in lst:
        if i == 'flick':
            switch = not switch 
        result.append(switch)
    return result