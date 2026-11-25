def solve(arr):
    a, b = arr[0], arr[1]
    for i in range(2, len(arr), 2):
        c, d = arr[i], arr[i + 1]
        a, b = a * c - b * d, a * d + b * c
    return [abs(a), abs(b)]