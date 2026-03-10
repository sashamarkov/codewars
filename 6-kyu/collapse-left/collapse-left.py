def operation_arguments(arr):
    r = []
    for x in arr:
        if callable(x):
            r[-1:] = [x(r[-1] if r else 0)]
        else:
            r.append(x)
    return r