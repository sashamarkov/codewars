def find(a, b, n):
    if n < 2:
        return (a, b)[n]
    seen = {}
    d = []
    while (a, b) not in seen:
        seen[(a, b)] = len(d)
        for c in map(int, str(a + b)):
            d.append(c)
            a, b = b, c
    start = seen[(a, b)]
    k = n - 2
    return d[k if k < start else start + (k - start) % (len(d) - start)]