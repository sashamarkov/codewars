def compute_ranks(number, games):
    stats = [[0, 0, 0] for _ in range(number)]
​
    for a, b, ga, gb in games:
        stats[a][1] += ga
        stats[a][2] += gb
        stats[b][1] += gb
        stats[b][2] += ga
        if ga > gb:
            stats[a][0] += 2
        elif ga < gb:
            stats[b][0] += 2
        else:
            stats[a][0] += 1
            stats[b][0] += 1
​
    def key(i):
        p, f, a = stats[i]
        return (p, f - a, f)
    
    order = sorted(range(number), key=key, reverse=True)
    positions = [0] * number
    place = 1
    for i, team in enumerate(order):
        if i > 0 and key(order[i - 1]) != key(team):
            place = i + 1
        positions[team] = place
    return positions