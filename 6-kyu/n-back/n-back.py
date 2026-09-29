def count_targets(n, sequence):
    return sum(sequence[i] == sequence[i - n] for i in range(n, len(sequence)))