from collections import Counter
​
def find_number(start, stop, string):
    diff = Counter(''.join(map(str, range(start, stop + 1)))) - Counter(string)
    return [num for num in range(start, stop + 1) if Counter(str(num)) == diff] if diff else []