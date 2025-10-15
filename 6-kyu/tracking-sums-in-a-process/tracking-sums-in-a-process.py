def track_sum(arr):
    sums = [sum(arr)]
    arr = sorted(set(arr), reverse=True)
    sums.append(sum(arr))
    diffs = [abs(a - b) for a, b in zip(arr, arr[1:])]
    unique_diffs = list(dict.fromkeys(diffs))
    return [sums + [sum(diffs), sum(unique_diffs)], unique_diffs]