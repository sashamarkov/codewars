def sflpf_data(val, nMax):
    s = [0] * (nMax + 1)
    l = [0] * (nMax + 1)
    for p in range(2, nMax + 1):
        if not s[p]:
            for m in range(p, nMax + 1, p):
                s[m] = s[m] or p
                l[m] = p
    return [x for x in range(4, nMax + 1) if s[x]  < x and s[x] + l[x] == val]