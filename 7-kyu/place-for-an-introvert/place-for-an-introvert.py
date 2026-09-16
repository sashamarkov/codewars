def introverted_seat(seats: str) -> str | None:
    s, n, best = seats, len(seats), None
    for i, c in enumerate(s):
        if c != '0':
            continue
        t = (i > 0 and s[i-1] in '01') + (i < n-1 and s[i+1] in '01')
        if t < 2 and (best is None or t < best[0]):
            best = (t, i)
            if not t: break
    return best and s[:best[1]] + '1' + s[best[1]+1:] or None