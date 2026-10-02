def nines(n):
    s = str(n)
    m = 0
    for i, c in enumerate(s):
        m += int(c) * 9 ** (len(s) - i - 1)
        if c == "9":
            break
    else:
        m +=1
    return n - m + 1