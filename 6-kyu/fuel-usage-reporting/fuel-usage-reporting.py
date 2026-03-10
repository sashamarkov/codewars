def total_kilometers(cons, petrol):
    return round(petrol/cons*100, 2)
​
def check_distance(d, c, p):
    if d > total_kilometers(c, p):
        return "You will need to refuel"
    return [[i, max(d-i,0), round(p - (i/100)*c, 2)] for i in range(0, d+1, 100)]