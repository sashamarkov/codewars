from math import prod
​
def find_us(n1, n2, k, prime_factors, digits):
    end = n1 + k * n2
    s = set(str(d) for d in digits)
    lcm = prod(prime_factors)
    start = ((n1 + lcm - 1) // lcm) * lcm
    return [m for m in range(start, end + 1, lcm) if s <= set(str(m))]