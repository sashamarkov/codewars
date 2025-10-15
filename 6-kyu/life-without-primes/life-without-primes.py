def solve(n):
    digits = set([0, 1, 4, 6, 8, 9])
    num = 1
    while n >= 0:
        if all(int(d) in digits for d in str(num)) and not is_prime(num):
            n -= 1
        num += 1
    return num - 1
​
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True