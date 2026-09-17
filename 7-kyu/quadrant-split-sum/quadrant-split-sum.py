def max_land_value(area):
    r, c = len(area), len(area[0])
    rm, cm = r // 2, c // 2
    return max(
        sum(area[i][j] for i in range(ri, re) for j in range(ci, ce))
        for ri, re in ((0, rm), (rm + r % 2, r))
        for ci, ce in ((0, cm), (cm + c % 2, c))
    )