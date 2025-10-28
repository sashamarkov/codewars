def elevator(left, right, call):
    if abs( right - call ) <= abs( left - call ):
        return "right"
    return "left"