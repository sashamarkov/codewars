def find_lineup(distances):
    lineup = [0] * len(distances)
    for i, d in enumerate(distances):
        if d >= len(distances) or lineup[d]:
            return []
        lineup[d] = i + 1
    if 0 in lineup:
        return []
    return lineup