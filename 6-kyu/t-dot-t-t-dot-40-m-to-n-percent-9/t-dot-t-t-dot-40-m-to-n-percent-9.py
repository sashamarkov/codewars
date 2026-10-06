def n_mod9(m, n):
    return sum(sum(map(int, str(x))) for x in range(m, n + 1)) % 9