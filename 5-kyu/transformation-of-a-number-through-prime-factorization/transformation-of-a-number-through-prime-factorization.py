def f(n):
    result = 1
    d = 2
    while d * d <= n:
        k = 0
        while n % d == 0:
            n //= d
            k += 1
        if k > 0:
            result *= k * d ** (k - 1)
        d += 1
    return result