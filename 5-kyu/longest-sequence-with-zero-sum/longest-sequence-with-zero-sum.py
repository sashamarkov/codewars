def max_zero_sequence(arr):
    n = 0
    first = {0: 0}
    a, b = 0, 0
    for j, x in enumerate(arr, start=1):
        n += x
        if n in first:
            i = first[n]
            if j - i > b - a:
                a, b = i, j
        else:
            first[n] = j
    return arr[a:b]