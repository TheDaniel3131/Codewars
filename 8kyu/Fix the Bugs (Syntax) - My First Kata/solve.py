def my_first_kata(a,b):
    if type(a) in [int] and type(b) in [int]:
        return a % b ++ b % a
    else:
        return False
    
    
    
def my_first_kata(a,b):
    #your code here
    if type(a) == int and type(b) == int:
        return a % b + b % a
    else:
        return False
    
    
def my_first_kata(a, b):
    try:
        return a % b + b % a
    except (TypeError, ZeroDivisionError):
        return False
    
    
def my_first_kata(a,b):
    return type(a) == type(b) == int and a % b + b % a