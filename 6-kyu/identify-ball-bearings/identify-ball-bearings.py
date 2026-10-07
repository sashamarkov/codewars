def identify_bb(bearings, weigh):
    args = [b for i, b in enumerate(bearings, 1) for _ in range(i)]
    n = len(bearings)
    return bearings[weigh(*args) - 5 * n * (n + 1) - 1]