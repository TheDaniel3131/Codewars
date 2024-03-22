def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1] + 1:
            return arr[i]
    return None


def first_non_consecutive(arr):
    if not arr: return 0
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]
        
def first_non_consecutive(arr):
    for i in range(len(arr)-1):
        if arr[i]+1!=arr[i+1]:
            return arr[i+1]
    return None

def first_non_consecutive(arr):
    num = arr[0] 
    
    for i in range(len(arr)):
        if num == arr[i]:
            num += 1
        else:
            return arr[i]
        
def first_non_consecutive(arr):
    return next((j for i, j in zip(arr, arr[1:]) if i + 1 != j), None)


def first_non_consecutive(a):
    i = a[0]
    for e in a:
        if e != i:
            return e
        i += 1
    return None