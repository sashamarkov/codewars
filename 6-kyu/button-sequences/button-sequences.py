def button_sequences(seq_r, seq_b):
    res = []
    current = None
    pr = pb = '0'
​
    for r, b in zip(seq_r, seq_b):
        rp = pr == '0' and r == '1'
        bp = pb == '0' and b == '1'
        rr = pr == '1' and r == '0'
        br = pb == '1' and b == '0'
​
        if current is None:
            if rp:
                res.append('R'); current = 'R'
            elif bp:
                res.append('B'); current = 'B'
        elif current == 'R' and rr:
            if b == '1':
                res.append('B'); current = 'B'
            else:
                current = None
        elif current == 'B' and br:
            if r == '1':
                res.append('R'); current = 'R'
            else:
                current = None
​
        pr, pb = r, b
​
    return ''.join(res)