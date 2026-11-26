def champion_rank(pilot: int, events: str) -> int:
    order = list(range(1, 21))
    t = events.split()
    for id, event in zip(t[::2], t[1::2]):
        id = int(id)
        if event == 'O':
            i = order.index(id)
            order[i], order[i - 1] = order[i - 1], order[i]
        elif id == pilot:
            return -1
        else:
            order.remove(id)
    return order.index(pilot) + 1