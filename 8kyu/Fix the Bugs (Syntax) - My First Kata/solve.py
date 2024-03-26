def my_first_kata(a,b):
    if type(a) in [int] and type(b) in [int]:
        return a % b ++ b % a
    else:
        return False