def find_zombies(matrix):
    rows, cols = len(matrix), len(matrix[0])
    target = matrix[0][0]
    result = [[0] * cols for _ in range(rows)]
    stack = [(0, 0)]
    while stack:
        r, c = stack.pop()
        if result[r][c]:
            continue
        result[r][c] = 1
        for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if 0 <= nr < rows and 0 <= nc < cols and not result[nr][nc] and matrix[nr][nc] == target:
                stack.append((nr, nc))
    return result