def find_spec_partition(n, k, com):
    q, r = divmod(n, k)
    return [q + 1] * r + [q] * (k - r) if com == 'max' else [n - k + 1] + [1] * (k - 1)