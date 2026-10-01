def prime_ant(n):
    arr = list(range(2, n + 3))
    p = 0
    while n:
        x = arr[p]
        if all(x % d for d in range(2, int(x**0.5) + 1)):
            p += 1
        else:
            q = next(d for d in range(2, x + 1) if x % d == 0)
            arr[p] //= q
            arr[p - 1] += q
            p -= 1
        n -= 1
    return p