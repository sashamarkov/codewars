from itertools import permutations
​
def mastermind(game):
    colours = ["Red", "Blue", "Green", "Orange", "Purple", "Yellow"]
    counts = {}
    for c in colours:
        r = game.check([c] * 4)
        if r == 'WON!':
            return
        counts[c] = sum(h in ('Black', 'White') for h in r)
    pool = [c for c, k in counts.items() for _ in range(k)]
    for g in set(permutations(pool)):
        if game.check(list(g)) == 'WON!':
            return 