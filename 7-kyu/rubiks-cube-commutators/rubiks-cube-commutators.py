def invert(m):
    if len(m) == 1: return m + "'"
    return m[0] if m.endswith("'") else m
​
def reverse_moves(moves):
    return [invert(m) for m in moves[::-1]]
​
def create_commutator(a, b):
    a_moves = a.split()
    b_moves = b.split()
    return " ".join(a_moves + b_moves + reverse_moves(a_moves) + reverse_moves(b_moves))