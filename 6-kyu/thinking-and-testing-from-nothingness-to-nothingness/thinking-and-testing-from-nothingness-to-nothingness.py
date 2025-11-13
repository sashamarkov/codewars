from re import search
def testit(s):
    return m[0].strip() if (m := search(r'\s[a-z]*(\s|$)',s)) else None