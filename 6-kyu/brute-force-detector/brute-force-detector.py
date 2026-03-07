def detect_brute_force(logs):
    fails = {}
    suspicious = set()
    for log in logs:
        ip, action = log.split(' ', 1)
        fails[ip] = 0 if 'SUCCESS' in action else fails.get(ip, 0) + 1
        if fails[ip] >= 3:
            suspicious.add(ip)
    return sorted(suspicious)