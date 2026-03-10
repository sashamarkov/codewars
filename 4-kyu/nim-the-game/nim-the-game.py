def choose_move(b):
    x = 0
    for p in b:
        x^=p
    if x:
        for i,p in enumerate(b):
            if p^x < p:
                return i, p - (p^x)
    return next((i, 1)for i,p in enumerate(b)if p)