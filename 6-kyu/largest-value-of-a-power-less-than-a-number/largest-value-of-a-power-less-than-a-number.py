def largest_power(n):
    if n == 1: return (0, -1)
    if n <= 4: return (1, -1)
    result = count = 0
    for a in range(2, int(n**0.5) + 1):
        val = a**2
        b = 2
        while val < n:
            if val > result:
                result, count = val, 1
            elif val == result:
                count += 1
            val *= a
            b += 1
    return (result, count)