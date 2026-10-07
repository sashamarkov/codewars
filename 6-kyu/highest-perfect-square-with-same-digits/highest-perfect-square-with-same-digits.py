from math import isqrt
from itertools import permutations
​
def next_perfectsq_perm(lower_limit, k): 
    n = isqrt(lower_limit) + 1
    while True:
        s = n ** 2
        if '0' not in str(s):
            squares = {p for p in map(int, map(''.join, permutations(str(s)))) if isqrt(p) ** 2 == p}
            if len(squares) == k:
                return max(squares)
        n += 1
        