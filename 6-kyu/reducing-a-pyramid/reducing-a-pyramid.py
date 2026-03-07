def reduce_pyramid(base):
    n = len(base)
    if n == 1:
        return base[0]
    coeff = 1
    result = base[0] * coeff
    for i in range(1, n):
        coeff = coeff * (n - i) // i
        result += base[i] * coeff
    return result