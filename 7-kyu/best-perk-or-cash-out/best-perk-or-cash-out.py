def pick(preferred, blacklisted, options):
    valid = [(chr(65+i), pct, skill) for i, (skill, pct) in enumerate(options) 
             if skill not in blacklisted]
    preferred_ops = [(idx, pct) for idx, pct, skill in valid if skill in preferred]
    if preferred_ops:
        return max(preferred_ops, key=lambda x: x[1])[0]
    neutral_ops = [(idx, pct) for idx, pct, skill in valid if skill not in preferred]
    if neutral_ops:
        return max(neutral_ops, key=lambda x: x[1])[0]
    return "D"