from collections import Counter
​
def path_finding(path):
    c = Counter(path)
    x = c['e'] - c['w']
    y = c['n'] - c['s']
    return (x, y) in [(3, 2), (-4, 3)]