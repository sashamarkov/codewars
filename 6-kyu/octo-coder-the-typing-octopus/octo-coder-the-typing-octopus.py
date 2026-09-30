def octopus(idea: str) -> str:
    result = []
    count = 0
    used = {}
    for c in idea:
        key = c.lower() if c.isalpha() else c
        mx = 2 if c.isdigit() else 1
        if used.get(key, 0) < mx:
            used[key] = used.get(key, 0) + 1
            result.append(c)    
        else:
            result.append('*')
        count += 1
        if count == 8:
            count = 0
            used = {}
    return "".join(result)