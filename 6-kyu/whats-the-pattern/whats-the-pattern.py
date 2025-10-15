def find_pattern(sequence):
    diffs = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
    for length in range(1, len(diffs) + 1):
        if len(diffs) % length == 0 and all(diffs[i] == diffs[i % length] for i in range(length, len(diffs))):
            return diffs[:length]