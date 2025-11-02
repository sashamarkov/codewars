def closed_brackets(s):
    a = b = 0  
    d = {'(': (1, 1), ')': (-1, -1), 'J': (-1, 1) }
    for char in s:
        a, b = a + d[char][0], b + d[char][1]
        if b < 0:
            return False
        a = max(a, 0)
    return a == 0