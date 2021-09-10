"""Circle."""
import math


def find_circle_info(d, x, y):
    """Circle is coming at the point."""
    r = d / 2
    S = math.pi * r ** 2
    P = 2 * r * math.pi
    distance = math.sqrt(((x - 0) ** 2) + ((y - 0) ** 2))
    if distance < r:
        place = "inside"
    elif distance > r:
        place = "outside"
    else:
        place = "perimeter"
    print(f"Circle with perimeter of {P} units and area of {S} units has point ({x}, {y}) on its {place}.")


if __name__ == "__main__":
    find_circle_info(10, 9, 8)
