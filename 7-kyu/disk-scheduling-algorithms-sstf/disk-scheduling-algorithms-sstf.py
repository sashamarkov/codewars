def sstf(request_queue, initial_head_position):
    q = list(request_queue)
    h = initial_head_position
    result = 0
    while q:
        j = min(range(len(q)), key=lambda i: abs(q[i] - h))
        x = q.pop(j)
        result += abs(x - h)
        h = x
    return result