import re
​
def math_test(picture, questions):
    names = re.findall(r'\s*(\w+)\s*', picture)
    names = [n for n in names if n and not n.startswith('_')]
    g = [names[i:i+3] for i in range(0, 9, 3)]
    p = {g[r][c]:(r,c) for r in range(3) for c in range(3)}
    r = []
    for q in questions.split('\n'):
        name = q[:q.index(':')]
        y,x = p[name]
        if 'left' in q: a = g[y][x-1] if x > 0 else 'nobody'
        elif 'right' in q: a = g[y][x+1] if x < 2 else 'nobody'
        elif 'upstairs' in q: a = g[y-1][x] if y > 0 else 'nobody'
        else: a = g[y+1][x] if y < 2 else 'nobody'
        r.append(q.replace('(?)', f'({a})'))
    return '\n'.join(r)