from collections import deque
​
def all_alone(house):
    rows, cols = len(house), len(house[0])
    x = next((r, c) for r in range(rows) for c in range(cols) if house[r][c] == 'X')
    seen = {x}
    q = deque([x])
    while q:
        r, c = q.popleft()
        if house[r][c] == 'o':
            return False
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and house[nr][nc] != '#':
                seen.add((nr, nc))    
                q.append((nr, nc))
    return True