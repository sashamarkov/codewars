def ant(grid, column, row, n, direction=0):
    grid = [r[:] for r in grid]
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
​
    for _ in range(n):
        if grid[row][column]:
            direction = (direction + 1) % 4
            grid[row][column] = 0
        else:
            direction = (direction - 1) % 4
            grid[row][column] = 1
​
        dr, dc = moves[direction]
        row += dr
        column += dc
​
        if row < 0:
            grid.insert(0, [0] * len(grid[0]))
            row = 0
        elif row >= len(grid):
            grid.append([0] * len(grid[0]))
        if column < 0:
            for r in grid: 
                r.insert(0, 0)
            column = 0
        elif column >= len(grid[0]):
            for r in grid: r.append(0)
    return grid