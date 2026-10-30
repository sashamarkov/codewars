def minimum_bonus(scores):
    result = [1] * len(scores)
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            result[i] = result[i - 1] + 1
    for i in range(len(scores) - 2, -1, -1):
        if scores[i] > scores[i + 1]:
            result[i] = max(result[i], result[i + 1] + 1)
    return sum(result)