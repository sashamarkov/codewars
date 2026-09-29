def mult_primefactor_sum(a, b):
    return [x for x in range(a, b + 1) if x == 1 or (not is_prime(x) and x % factors_sum(x) == 0)]
​
def is_prime(n):
     return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))
​
def factors_sum(n):
    s, d = 0, 2
    while d * d <= n:
        while n % d == 0:
            s += d
            n //= d
        d += 1
    return s + n if n > 1 else s