def binarray(s)->int:
    seen = {0: -1}
    result, p = 0, 0
    for i, v in enumerate(s):
        p += 2 * v - 1
        result = max(result, i - seen.setdefault(p, i))
    return result