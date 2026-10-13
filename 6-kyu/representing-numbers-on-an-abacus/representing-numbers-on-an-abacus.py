def create_abacus(n):
    d = [int(c) for c in f'{n:09d}']
    return '\n'.join(_upper(d) + ['-' * 9] + _lower(d))
​
def _upper(d):
    return [''.join(' ' if x >= 5 else '*' for x in d),
            ''.join('*' if x >= 5 else ' ' for x in d)]
    
def _lower(d):
    return [''.join('*' if r < x % 5 else ' ' if r == x % 5 else '*' for x in d)
            for r in range(5)]
​
def read_abacus(abacus):
    rows = abacus.split('\n')
    return int(''.join(str(_digit(rows, i)) for i in range(9)))
​
def _digit(rows, i):
    v = 5 if rows[1][i] == '*' else 0
    for r in rows[3:8]:
        if r[i] == '*':
            v += 1
        else:
            break
    return v