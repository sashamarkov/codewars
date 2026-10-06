from collections import Counter
​
def calculate_cart_total(contents):
    c = sorted(Counter(contents).values(), reverse=True) + [0] * 4
    c1,  c2, c3, c4 = c[:4]
    total = sum(c[:4])
    best = float('+inf')
    for n4 in range(c4 + 1):
        for n3 in range(c3 - n4 + 1):
            for n2 in range(c2 - n3 - n4 + 1):
                n1 = total - n4 * 4 - n3 * 3 - n2 * 2
                best = min(best, n4 * 32 + n3 * 27 + n2 * 19 + n1 * 10)
    return best