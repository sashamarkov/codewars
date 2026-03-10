def combos(n):
    dp = [[] for _ in range(n+1)]
    dp[0] = [[]]
    for i in range(1, n+1):
        for j in range(i, n+1):
            for combo in dp[j-i]:
                dp[j].append(combo + [i])
    return dp[n]