def test_it(arr):
    items = [x for x in arr if x != '?']
    cs = {x.split()[0] for x in items}
    ss = {x.split()[1] for x in items}
    return ({(f"{c} {s}") for c in cs for s in ss} - set(items)).pop()