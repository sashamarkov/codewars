def sum_pow_dig_seq(start, n, k):
    seq = []
    seen = {}
    x = start
    while x not in seen:
        seen[x] = len(seq)
        seq.append(x)
        x = sum(int(d) ** n for d in str(x))
    h = seen[x]
    cyc_patt_arr = seq[h:]
    patt_len = len(cyc_patt_arr)
    last_term = seq[k] if k < len(seq) else cyc_patt_arr[(k - h) % patt_len]
    return [h, seq[h:], patt_len, last_term]
​