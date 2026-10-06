def corner_fill(square):
    if not square:
        return []
    result = []
    top = left = 0
    bottom = right = len(square) - 1
    fwd = True
    while top <= bottom:
        if fwd:
            result += [square[top][c] for c in range(left, right + 1)]
            result += [square[r][right] for r in range(top + 1, bottom + 1)]
        else:
            result += [square[r][right] for r in range(bottom, top - 1, -1)]
            result += [square[top][c] for c in range(right - 1, left - 1, -1)]
        top += 1
        right -= 1
        fwd = not fwd
    return result