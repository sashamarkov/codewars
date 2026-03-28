from functools import reduce
​
def poly_from_roots(r):
    return reduce(poly_multiply, [[-x, 1] for x in r], [1])