def sum_array(arr):
    if arr == None:
        return 0;
    elif len(arr) < 3:
        return 0;
    else:
        return sum(arr) - max(arr) - min(arr)