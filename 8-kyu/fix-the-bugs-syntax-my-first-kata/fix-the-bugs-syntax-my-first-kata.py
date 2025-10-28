def my_first_kata(a,b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        return False
    if a == 0 or b == 0:
        return False
    return a % b + b % a