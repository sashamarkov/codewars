def create_keypad():
    keypad = {}
    layout = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        ['0', ' ', ' ']
    ]
    for y, row in enumerate(layout):
        for x, char in enumerate(row):
            if char != ' ':
                keypad[int(char)] = (x, y)
    return keypad, {v: k for k, v in keypad.items()}
​
def move(pos, direction):
    x, y = pos
    if direction == '↑':
        return (x, y-1)
    elif direction == '↓':
        return (x, y+1)
    elif direction == '←':
        return (x-1, y)
    elif direction == '→':
        return (x+1, y)
    return pos
​
def dec_arrow_pin_code(s):
    keypad, rev_keypad = create_keypad()
    result = [int(s[0])]
    pos = keypad[result[0]]
    i = 1
    while i < len(s):
        if s[i] == '*':
            repeat = int(s[i+1])
            result += [result[-1]] * repeat
            i += 2
        else:
            pos = move(pos, s[i])
            if pos not in rev_keypad:
                return []
            result.append(rev_keypad[pos])
            i += 1
    return result