def set_table(the_dead):
    seats = [None] * 12
    for name in the_dead:
        if all(seats):
            break
        c = corner(name)
        def key(i):
            seat = i + 1
            d = dist(seat, c)
            if seat == ((c - d - 1) % 12 + 1):
                return (d, 0)
            return (d, 1)
        free = [i for i in range(12) if seats[i] is None]
        m = min(free, key=key)
        seats[m] = name        
    return [s or "_____" for s in seats]
​
def corner(name):
    c = name[0]
    if c in 'QUTHCRDMZ': return 1
    if c in 'WEVOXING':  return 4
    if c in 'JFABKPLY':  return 7
    return 10
​
def dist(a, b):
    d = abs(a - b)
    return min(d, 12 - d)