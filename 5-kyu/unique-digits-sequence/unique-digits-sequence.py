def find_num(n):
    cur = 0
    seen = {0}
    for _ in range(n):
        t = set(str(cur))
        cur = 0
        while cur in seen or t & set(str(cur)):
            cur += 1
        seen.add(cur)
    return cur