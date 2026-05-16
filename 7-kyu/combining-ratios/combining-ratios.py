from math import gcd
​
def merge_ratios(r1, r2):
    (a, x), (y, c) = (map(int, r.split(':')) for r in (r1, r2))
    l = x * y // gcd(x, y)
    g = gcd(a * l // x, gcd(l, c * l // y))
    return f"{a * l // x // g}:{l // g}:{c * l // y // g}"