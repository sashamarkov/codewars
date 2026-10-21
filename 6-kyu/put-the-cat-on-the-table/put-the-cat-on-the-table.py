def put_the_cat_on_the_table(cat, room):
    if not _in_room(cat, room):
        return "NoCat"
    table = _find_table(room)
    if table is None:
        return "NoTable"
    return _route(cat, table)
​
​
def _in_room(cat, room):
    r, c = cat
    return 0 <= r < len(room) and 0 <= c < len(room[0])
​
​
def _find_table(room):
    return next(((i, j) for i, row in enumerate(room) for j, v in enumerate(row) if v), None)
​
​
def _route(cat, table):
    r, c = cat
    tr, tc = table
    return 'D' * (tr - r) + 'U' * (r - tr) + 'R' * (tc - c) + 'L' * (c - tc)