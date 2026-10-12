def missing(s):
    for length in range(1, len(s) // 2 + 1):
        if s[0] == '0':
            continue
        prev = int(s[:length])
        i = length
        skip = None
        while i < len(s):
            if s.startswith(str(prev + 1), i):
                prev += 1
                i += len(str(prev))
            elif skip is None and s.startswith(str(prev + 2), i):
                skip = prev + 1
                prev += 2
                i += len(str(prev))
            else:
                break
        if i == len(s) and skip is not None:
            return skip
    return -1