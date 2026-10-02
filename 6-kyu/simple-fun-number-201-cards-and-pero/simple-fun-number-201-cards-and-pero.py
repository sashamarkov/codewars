from collections import Counter
​
def cards_and_pero(s):
    cards = [s[i:i+3] for i in range(0, len(s), 3)]
    if len(set(cards)) < len(cards):
        return [-1, -1, -1, -1]
    cnt = Counter(c[0] for c in cards)
    return [13 - cnt[c] for c in 'PKHT']