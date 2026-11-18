def proc_arr_int(lst):
    divisor_counts = [(n, count_divisors(n)) for n in lst]
    max_divisors = max(count for _, count in divisor_counts)
    best = sorted(n for n, count in divisor_counts if count == max_divisors)
    primes = sum(1 for n in lst if is_prime(n))
    return [len(lst), primes, [max_divisors, best]]
​
def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1 if i * i == n else 2
        i += 1
    return count
​
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True