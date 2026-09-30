def find_super_man(s):
    s_lower = s.lower()
    
    if "superman" in s_lower:
        return "Are you crazy?"
    
    def check(target):
        idx = 0
        last_pos = -2
        for i, ch in enumerate(s_lower):
            if idx < len(target) and ch == target[idx]:
                if i == last_pos + 1:
                    continue
                idx += 1
                last_pos = i
        return idx == len(target)
    
    if check("superman") or check("superman"[::-1]):
        return "Hi, SuperMan!"
    
    return "Are you crazy?"