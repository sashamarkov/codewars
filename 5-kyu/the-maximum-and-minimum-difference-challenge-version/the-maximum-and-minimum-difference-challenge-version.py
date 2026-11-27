from itertools import chain
​
def max_and_min(seq1, seq2): 
    max_diff = max(abs(max(seq1) - min(seq2)), abs(max(seq2) - min(seq1)))
    t = sorted(chain(((v, 0) for v in seq1), ((v, 1) for v in seq2)))
    min_diff = min(
        b[0] - a[0]
        for a, b in zip(t, t[1:])
        if a[1] != b[1]
    )
    return max_diff, min_diff    