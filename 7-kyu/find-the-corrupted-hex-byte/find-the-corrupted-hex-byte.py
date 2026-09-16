HEX = set("0123456789ABCDEF")
​
def find_corrupted_byte(dump):
    for i, b in enumerate(dump):
        if len(b) != 2 or not all(c in HEX for c in b):
            return i
    return -1