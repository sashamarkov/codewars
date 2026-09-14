from math import log2
from collections import Counter
​
def entropy(message: str) -> float:
    s = [c for c in message if c != ' ']
    if not s:
        return 0.0
    return -sum((c / len(s)) * log2(c / len(s)) for c in Counter(s).values())