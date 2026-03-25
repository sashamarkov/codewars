def breach_attempts(hackers, security_level, increase):
    breaches = 0
    for skill in hackers:
        if skill > security_level:
            breaches += 1
        else:
            security_level += increase
    return breaches