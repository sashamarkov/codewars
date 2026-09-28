from math import factorial
from collections import Counter
​
def proc_arr(arr):
    counter = Counter(arr)
    perms = factorial(len(arr))
    for k in counter.values():
        perms //= factorial(k)
    return [
        perms,
        int(''.join(sorted(arr))),
        int(''.join(sorted(arr, reverse=True)))
    ]
​