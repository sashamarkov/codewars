from math import ceil
​
def branch(n):
    if n == 1:
        return 0
    r = (ceil(n ** 0.5) // 2) * 2
    return (n - 2) // r  - r + 2