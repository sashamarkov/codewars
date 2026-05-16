def encode(n):
    r = [n & 0x7F]
    while n := n >> 7:
        r.append(n & 0x7F | 0x80)
    return r[::-1]
​
​
def decode(data):
    n = 0
    for b in data:
        n = n << 7 | b & 0x7F
        if not b & 0x80: return n