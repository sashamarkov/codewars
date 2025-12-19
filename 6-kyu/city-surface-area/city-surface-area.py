def city_surface_area(_map):
    rows, cols = len(_map), len(_map[0])
    total = rows * cols
    for r in range(rows):
        for c in range(cols):
            h = _map[r][c]
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    total += max(0, h - _map[nr][nc])
                else:
                    total += h
    return total