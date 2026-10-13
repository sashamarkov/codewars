from collections import Counter
​
def count_digits(num, rounds):
    for _ in range(rounds):
        c = Counter(str(num))
        num = int(''.join(f'{v}{k}' for k, v in c.items()))
    return [int(f'{v}{k}') for k, v in c.items()]