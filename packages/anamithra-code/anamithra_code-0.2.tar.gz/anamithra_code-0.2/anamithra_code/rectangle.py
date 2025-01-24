def rectangle_area(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Both length and width must be numbers.")
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width
