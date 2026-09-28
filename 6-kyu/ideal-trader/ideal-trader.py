from math import prod
​
def ideal_trader(prices):
    return prod(b / a for a, b in zip(prices, prices[1:]) if b > a)
​