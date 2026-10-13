def is_valid_train_arrangement(before, after):
    x = [(i, c) for i, c in enumerate(before) if c != '.']
    y = [(i, c) for i, c in enumerate(after) if c != '.']
    return (len(before) == len(after) and
            len(x) == len(y) and
            all(c1 == c2 and (i2 - i1) * (1 - 2 * (c1 == '<')) >= 0
                for (i1, c1), (i2, c2) in zip(x, y)))