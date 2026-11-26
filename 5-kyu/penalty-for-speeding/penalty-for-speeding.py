from functools import cmp_to_key
​
def penalty(numbers):
    return ''.join(sorted(numbers, key=cmp_to_key(lambda a, b: (a + b > b + a) - (a + b < b + a))))