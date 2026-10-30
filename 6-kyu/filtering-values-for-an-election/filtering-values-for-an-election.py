import math
​
def filter_val(lst):
    data = list(lst)
    while True:
        m = mean(data)
        s = std_dev(data)
        lo, hi = m - 2.5 * s, m + 2.5 * s
        new_data = [x for x in data if lo <= x <= hi]
        if len(new_data) == len(data):
            break
        data = new_data
    m = mean(data)
    s = std_dev(data) / math.sqrt(len(data))
    return [[len(lst), len(data)], m, s]
​
def mean(data):
    return sum(data) / len(data)
​
def std_dev(data):
    m = mean(data)
    return math.sqrt(sum((x - m) ** 2 for x in data) / len(data))