def locate_entrance(office):
    for y in range(len(office)):
        row = office[y]
        for x in range(len(row)):
            if row[x] == '.':
                if x == 0 or row[x-1] == ' ':
                    return (x, y)
                if x == len(row) - 1 or (x + 1 < len(row) and row[x+1] == ' '):
                    return (x, y)
                if y == 0 or x >= len(office[y-1]) or office[y-1][x] == ' ':
                    return (x, y)
                if y == len(office) - 1 or x >= len(office[y+1]) or office[y+1][x] == ' ':
                    return (x, y)
    return (0, 0)