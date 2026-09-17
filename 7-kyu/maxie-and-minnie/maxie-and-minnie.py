def swap(n):
    s = str(n)
    mx = mn = n
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            m = int(s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:])
            if s[j] > s[i]:
                   mx = max(mx, m)
            if s[j] < s[i] and (i or s[j] != '0'):
                   mn = min(mn, m)
    return mx, mn