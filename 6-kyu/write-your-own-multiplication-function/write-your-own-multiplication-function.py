def multiply(n, f):
    result = zero
    while n > zero:
        if n & one:
            result += f
        f = f << one
        n = n >> one
    return result