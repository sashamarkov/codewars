SQUARES = {'0':'0','1':'1','4':'2','9':'3','16':'4','25':'5','36':'6','49':'7','64':'8','81':'9'}
​
def unsquare_digits(n):
    s = str(n)
    dp = [None] * (len(s) + 1)
    dp[-1] = ""
    for i in range(len(s) - 1, -1, -1):
        for k in (1, 2):
            if i + k > len(s):
                continue
            chunk = s[i:i+k]
            if chunk in SQUARES and dp[i+k] is not None:
                m = SQUARES[chunk] + dp[i+k]
                if dp[i] is None or int(m) < int(dp[i]):
                    dp[i] = m
    if dp[0] is not None:
        return int(dp[0])
    return None