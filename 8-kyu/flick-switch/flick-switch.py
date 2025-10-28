def flick_switch(lst):
    result = [True] * len(lst)
    v = True
    for i in range(0, len(lst)):
        if lst[i] == 'flick':
            v = not v
        result[i] = v
    return result