def upper_triangular(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i):
            if mat[i][j] != 0:
                return False
    return True
​
def lower_triangular(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n):
            if mat[i][j] != 0:
                return False
    return True