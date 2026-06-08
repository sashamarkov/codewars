import math
​
def entropy(pwd):
    pools = {
        "abcdefghijklmnopqrstuvwxyz": 26,
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 26,
        "0123456789": 10,
        r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""": 32
    }
    R = sum(size for chars, size in pools.items() if any(c in chars for c in pwd))
    return len(pwd) * math.log2(R)