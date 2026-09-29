from itertools import cycle
​
def max_hexagon_beam(n, seq):
    h = 2 * n - 1
    values = cycle(seq)
    horz = [0] * h
    diag_dr = [0] * h
    diag_dl = [0] * h
    for r in range(h):
        length = n + min(r, h - 1 - r)
        for c in range(length):
            v = next(values)
            idx_h = r
            idx_dr = c + max(0, r - n + 1)
            idx_dl = c + max(0, n - 1 - r)
            horz[idx_h] += v
            diag_dr[idx_dr] += v
            diag_dl[idx_dl] += v
    return max(max(horz), max(diag_dr), max(diag_dl))