def f(n):
    m = 10**9 + 7
    n_mod = n % m
    return (pow(2, n + 1, m) * (n_mod * n_mod - 2 * n_mod + 3) % m - 6) % m