def triangle(row):
    n = len(row)
    if n == 1:
        return row
    color_map = {'R': 0, 'G': 1, 'B': 2}
    a = [color_map[c] for c in row]
    total = 0
    m = n - 1
    power = 1 if (m % 2 == 0) else 2  # 2^(m) mod 3 is 1 if m even, 2 if odd
    
    for i in range(n):
        c = comb_mod(m, i)
        coeff = (c * power) % 3
        total = (total + coeff * a[i]) % 3
    return "RGB"[total]
​
def comb_mod(m, k):
    # Compute C(m, k) mod 3 using Lucas's theorem
    result = 1
    p = 3
    while m > 0 or k > 0:
        md = m % p
        kd = k % p
        if kd > md:
            return 0
        if md == 0:
            comb = 1 if kd == 0 else 0
        elif md == 1:
            comb = 1 if kd == 0 or kd == 1 else 0
        elif md == 2:
            if kd == 0 or kd == 2:
                comb = 1
            else:
                comb = 2
        result = (result * comb) % p
        m = m // p
        k = k // p
    return result