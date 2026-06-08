from math import comb
​
def moser():
    n = 1
    while True:
        yield comb(n, 4) + comb(n, 2) + 1
        n += 1