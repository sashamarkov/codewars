def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    samecase = (a.isupper() and b.isupper()) or (a.islower() and b.islower())
    return int(samecase)