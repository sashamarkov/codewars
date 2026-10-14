from preloaded import ANIMALS
from itertools import groupby
​
def road_kill(photo):
    group = lambda s: [(c, len(list(x))) for c, x in groupby(s)]
    f = group(photo.replace('=', ''))
    matched = lambda h: len(f) == len(h) and all(a == b and n >= m for (a, n), (b, m) in zip(f, h))
    return next((a for a in ANIMALS if matched(group(a)) or matched(group(a)[::-1])), '??')