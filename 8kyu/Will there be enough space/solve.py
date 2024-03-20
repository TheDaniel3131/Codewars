def enough(cap, on, wait):
    return (on + wait) - cap if (on + wait) > cap else 0
    
    
def enough(cap, on, wait):
    return max(0, wait - (cap - on))