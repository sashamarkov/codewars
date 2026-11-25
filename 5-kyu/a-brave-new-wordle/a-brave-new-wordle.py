from collections import Counter
​
def resolver(guess, solution):
    result = ['b'] * 5
    remaining = Counter(solution)
    for i in range(5):
        if guess[i] == solution[i]:
            result[i] = 'g'
            remaining[guess[i]] -= 1
​
    for i in range(5):
        if result[i] == 'g':
            continue
        if remaining[guess[i]] > 0:
            result[i] = 'y'
            remaining[guess[i]] -= 1
    return ''.join(result)