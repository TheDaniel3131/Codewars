def set_alarm(employed, vacation):
    if employed == 1 and vacation == 1:
        return 0
    elif employed == 1 and vacation == 0:
        return 1
    elif employed == 0 and vacation == 1:
        return 0
    else:
        return 0
    
    
def set_alarm(employed, vacation):
    return employed and not vacation


def set_alarm(employed, vacation):
    return employed==1 and vacation==0

def set_alarm(employed, vacation):
    return employed > vacation