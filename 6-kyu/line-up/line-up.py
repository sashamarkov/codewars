def line_up(hints):
    left, right = {}, {}
    for person, _, other, _, _, side in map(str.split, hints):
        if side == "left":
            left[person], right[other] = other, person
        else:
            right[person], left[other] = other, person
    first = next(p for p in right.keys() if p not in left)
    queue = [first]
    while queue[-1] in right:
        queue.append(right[queue[-1]])
    return queue