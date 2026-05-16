import re
​
def restore_code(tokens):
    ops = {"set": "=", "add": "+=", "sub": "-="}
    return "\n".join(f"{a}{ops[c]}{b}" for c, a, b in tokens if c in ops and a.isalpha() and re.fullmatch(r'-?\d+|[a-zA-Z]+', b))