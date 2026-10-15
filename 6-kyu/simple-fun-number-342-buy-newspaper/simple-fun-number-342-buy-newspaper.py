def buy_newspaper(s1, s2):
    if not s2:
        return 0
    if not s1 or not set(s2) <= set(s1):
        return -1
    count, pos = 1, 0
    for c in s2:
        i = s1.find(c, pos)
        if i == -1:
            count += 1
            pos = s1.find(c) + 1
        else:
            pos = i + 1
    return count