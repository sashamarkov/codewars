def compress(raw):
    result = []
    i = 0
    j = 0
    n = len(raw)
    while i < n:
        if (i + 1) < n and raw[i] == raw[i + 1]:
            j = i
            while (j + 1) < n and raw[j + 1] == raw[i]:
                j += 1
            result.append(f'{raw[i]}*{j - i + 1}')
        elif (i + 2) < n and raw[i+1] - raw[i] == raw[i+2] - raw[i+1]:
            step = raw[i + 1] - raw[i]
            j = i + 1
            while (j + 1) < n and raw[j + 1] - raw[j] == step:
                j += 1
            result.append(f'{raw[i]}-{raw[j]}' + ('' if abs(step) == 1 else f'/{abs(step)}'))
        else:
            j = i
            result.append(str(raw[i]))
        i = j + 1
    return ','.join(result)