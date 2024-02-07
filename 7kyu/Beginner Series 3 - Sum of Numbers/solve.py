def get_sum(a,b):
    # Test Case 6: (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
    if a == b:
        return a or b;
    elif a < b:
        print(sum(range(-1, 3)))
        return sum(range(a, b+1))
    else:
        return sum(range(b, a+1))
    
# output print: 2