def jumbler(indices):
    a, n = indices[:], 0
    while a[0]:
        a.insert(0, a.pop(a[0]))
        n += 1
    return n