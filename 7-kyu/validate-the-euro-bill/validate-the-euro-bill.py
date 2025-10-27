def validate_euro(serial):
    return (sum(int(d) for d in serial[2:]) + sum(ord(c) - 64 for c in serial[:2]) - 1) % 9 == 6