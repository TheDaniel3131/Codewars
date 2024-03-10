def solve(arr):
    arr.sort()
    minimum_positive_number = 1
    for i in arr:
        if i <= minimum_positive_number:
            minimum_positive_number += i
    return minimum_positive_number



# other methods I learned

from itertools import accumulate

def solve(arr):
    arr = sorted(arr)
    return next((x+1 for x, i in zip(accumulate([0]+arr), arr+[0]) if i > x + 1), sum(arr)+1)
Best Practices2Clever2
 0ForkCompare with your solutionLink


def solve(xs):
    m = 0
    for x in sorted(xs):
        if x > m + 1:
            break
        m += x
    return m + 1