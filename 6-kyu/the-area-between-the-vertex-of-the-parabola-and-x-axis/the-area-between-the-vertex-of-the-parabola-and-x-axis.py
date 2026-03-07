def area(a, b, c):
    d = b * b - 4 * a * c
    if d <= 0:
        return 0
    
    sd = d ** 0.5
    x1 = (-b - sd) / (2*a)
    x2 = (-b + sd) / (2*a)
    if x1 > x2:
        x1, x2 = x2, x1
    
    def f(x):
        return (a/3)*x**3 + (b/2)*x**2 + c*x
    return abs(f(x2) - f(x1))