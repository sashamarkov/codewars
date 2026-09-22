def even_magic(n):
    a = [[i * n + j + 1 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            r, c = i % 4, j % 4
            if r == c or r + c == 3:
                a[i][j] = n * n + 1 - a[i][j]
    return a