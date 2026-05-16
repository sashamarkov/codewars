def solve(waves: list[list[str]], prerequisites: list[tuple[str, str]]) -> bool:
    wave_index = {}
    for i, wave in enumerate(waves):
        for pkg in wave:
            if pkg in wave_index:
                return False
            wave_index[pkg] = i
    
    for a, b in prerequisites:
        if a not in wave_index or b not in wave_index:
            return False
        if wave_index[a] <= wave_index[b]:
            return False
    return True