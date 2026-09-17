from functools import reduce
​
def evaluate_polynomial(coefficients: list[int], x: int) -> int:
    return reduce(lambda a, b: a * x + b, coefficients, 0)