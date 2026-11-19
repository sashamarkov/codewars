def target_game(values):
    a, b = 0, 0
    for v in values:
        b, a = a, max(a, b + v)
    return a
​