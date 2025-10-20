def square(a, b):
    lo, hi = 1, int(a + b) // 4
    while lo <= hi:
        mid = (lo + hi) // 2
        if a // mid + b // mid >= 4:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi