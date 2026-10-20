def plus_or_minus(variables, test):
    weights = [3 ** (len(variables) - 1 - i) for i in range(len(variables))]
    r = test(weights)
    signs = []
    for w in weights:
        if r > 0:
            signs.append('+')
            r -= w
        else:
            signs.append('-')
            r += w
    result = ''.join(s + c for s, c in zip(signs, variables)).lstrip('+')
    return result