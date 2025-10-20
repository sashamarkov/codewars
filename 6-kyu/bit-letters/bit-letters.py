def bit_letter(n):
    result = []
    for byte in n:
        p = byte >> 6
        c = (byte >> 5) & 1
        l = byte & 31
        char = (' ' if p == 1 else '') + chr((65 if c else 97) + l)
        if p == 2: 
            char += ','
        if p == 3:
            char += '.'
        result.append(char)
    return ''.join(result)