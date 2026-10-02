LEN = {'mm': 1, 'cm': 10, 'dm': 100, 'm': 1000, 'km': 10**6}
TIME = {'ms': 1, 's': 1000, 'm': 60000, 'h': 3600000, 'd': 86400000}
DIGITS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
​
def testit(a):
    units = {x.lstrip(DIGITS) for x in a}
    if units <= LEN.keys():
        coef = LEN
    elif units <= TIME.keys():
        coef = TIME
    else:
        return None
    return sorted(a, key=lambda x: int(x.rstrip(LETTERS)) * coef[x.lstrip(DIGITS)])