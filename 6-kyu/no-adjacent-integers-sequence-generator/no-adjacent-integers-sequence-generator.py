def generate_sequence(lower, upper):
    return [*range(lower + 1, upper, 2), *range(lower, upper, 2)]