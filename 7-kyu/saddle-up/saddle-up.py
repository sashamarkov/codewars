def find_saddle_points(matrix):
    rows, cols = len(matrix), len(matrix[0])
    mins = [min(row) for row in matrix]
    maxs = [max(matrix[i][j] for i in range(rows)) for j in range(cols)]
    return [(i, j) for i in range(rows) for j in range(cols)
            if matrix[i][j] == mins[i] and matrix[i][j] == maxs[j]]