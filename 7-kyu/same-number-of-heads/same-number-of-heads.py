def split_coins(coins, k):
    return [coin.flip() for coin in coins[:k]], coins[k:]