from itertools import combinations
​
def bananas(s):
    banana = "banana"
    result = set()
    for indexes in combinations(range(len(s)), 6):
        row = ['-'] * len(s)
        for i, c in zip(indexes, banana):
            if s[i] != c:
                break    
            row[i] = c
        else:
            result.add(''.join(row))
    return result