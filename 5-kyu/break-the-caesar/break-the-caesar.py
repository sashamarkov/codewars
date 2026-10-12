def break_caesar(message):
    base = (ord('a'), ord('A'))
    def score(k):
        text = ''.join(
            chr((ord(c) - base[c.isupper()] - k) % 26 + base[c.isupper()])
            if c.isalpha() else ' '
            for c in message
        )
        return sum(w in WORDS for w in text.lower().split())
    return max(range(26), key=score)