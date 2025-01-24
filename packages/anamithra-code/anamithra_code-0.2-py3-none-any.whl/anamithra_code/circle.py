import math

def circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("The radius must be a number.")
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    return math.pi * radius ** 2
