from math import comb
​
def surjections(n: int, k: int) -> int:
    return sum((-1)**i * comb(k, i) * (k - i)**n for i in range(k + 1))