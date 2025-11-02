def simple_sum(x, y):
    return (y and simple_sum(x ^ y, (x & y) << 1)) or x