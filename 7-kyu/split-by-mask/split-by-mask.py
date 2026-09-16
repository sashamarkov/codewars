def split_by_mask(strng, mask):
    if sum(mask) != len(strng):
        return None
    it = iter(strng)
    return [''.join(next(it) for _ in range(m)) for m in mask]