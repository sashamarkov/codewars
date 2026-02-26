import math
import re
from functools import reduce
​
def has_integer_roots(equation):
    left, right = equation.split('=')
    coeffs, n = get_coefficients(left), int(right)
    g = reduce(math.gcd, coeffs, 0)
    return n % abs(g) == 0
​
def get_coefficients(left):
    terms = re.findall(r'[+-]?\d*[a-z]', left)
    return [parse_coefficient(term) for term in terms]
​
def parse_coefficient(term):
    coef_str = term[:-1]
    if coef_str == '' or coef_str == '+':
        return 1
    if coef_str == '-':
        return -1
    return int(coef_str)