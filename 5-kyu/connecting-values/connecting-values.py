Coord = tuple[int, int]
​
def connected_values(arr: list[list[int]], val: int, coord: Coord) -> set[Coord]:
    rows, cols = len(arr), len(arr[0]) if arr else 0
    r0, c0 = coord
    if not (0 <= r0 < rows and 0 <= c0 < cols) or arr[r0][c0] != val:
        return set()
​
    result, stack = set(), [coord]
    while stack:
        r, c = stack.pop()
        if (r, c) in result:
            continue
        result.add((r, c))
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if (dr or dc) and 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in result and arr[nr][nc] == val:
                    stack.append((nr, nc))
    return result