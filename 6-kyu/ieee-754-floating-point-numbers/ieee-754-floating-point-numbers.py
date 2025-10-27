from struct import pack, unpack
​
def float_to_IEEE_754(f):
    packed = pack('>d', f)
    bits = bin(unpack('>Q', packed)[0])[2:].zfill(64)
    return f"{bits[0]} {bits[1:12]} { bits[12:]}"