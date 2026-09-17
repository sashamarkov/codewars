from math import pi
from re import findall
​
MM_PER_INCH = 25.4
MM_PER_KM = 1_000_000
​
def tire_rotations(tire_size: str, distance_km: float) -> float:
    w, a, r = map(int, findall(r"\d+", tire_size))
    diameter = r * MM_PER_INCH + 2 * w * a / 100
    return distance_km * MM_PER_KM / (pi * diameter)