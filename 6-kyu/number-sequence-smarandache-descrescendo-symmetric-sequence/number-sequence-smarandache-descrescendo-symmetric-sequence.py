def solve(n, bound):
    t = p = 0
    for k in range(1, bound + 1):
        for i in [*range(1, k + 1), *range(k - 1, 0, -1)]:
            if i == bound:
                return t
            p += 1
            t += i * (p % n == 1 < p)