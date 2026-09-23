def xor_reduction(m, n):
    f = lambda x: [x, 1, x + 1, 0][x % 4]
    return f(n) ^ f(m - 1)