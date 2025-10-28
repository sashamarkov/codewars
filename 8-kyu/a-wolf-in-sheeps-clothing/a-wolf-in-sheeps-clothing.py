def warn_the_sheep(queue):
    n = len(queue)
    for i in range(0, n-1):
        if queue[i] == "wolf":
            return "Oi! Sheep number {0}! You are about to be eaten by a wolf!".format(str(n - i - 1))
    return "Pls go away and stop eating my sheep"