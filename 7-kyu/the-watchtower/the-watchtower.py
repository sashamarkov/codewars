import re
​
def watchtower(s):
    return re.sub(r'[a-z]', lambda m: m[0] if any(
        abs(m.start() - t.start()) <= ord(t[0]) - 64
        for t in re.finditer(r'[A-Z]', s)) else '', s)