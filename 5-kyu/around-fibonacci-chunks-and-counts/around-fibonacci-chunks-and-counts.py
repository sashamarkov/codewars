from collections import Counter
​
def around_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    s = str(a)
    c = Counter(s)
    maxcnt = max(c.values())
    digit = min(int(d) for d, v in c.items() if v == maxcnt)
    r = len(s) % 25 or 25
    last_chunk = s[-r:]
    return f"Last chunk {last_chunk}; Max is {maxcnt} for digit {digit}"