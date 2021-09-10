"""Polar and cartesian points converter."""
import math


def convert_polar_to_cartesian(r, phi):
    """"Part one."""
    rad = math.radians(phi)
    x = r * math.cos(rad)
    y = r * math.sin(rad)
    x = round(x, 2)
    y = round(y, 2)
    return (x, y)


def convert_cartesian_to_polar(x, y):
    """Part two."""
    r = math.sqrt(x ** 2 + y ** 2)
    conor = 0
    if x > 0:
        conor = math.degrees(math.atan(y / x))
    if x < 0 and y >= 0:
        conor = math.degrees(math.atan(y / x) + math.pi)
    if x < 0 and y < 0:
        conor = math.degrees(math.atan(y / x) - math.pi)
    if x == 0 and y > 0:
        conor = math.degrees(math.pi / 2)
    if x == 0 and y < 0:
        conor = math.degrees(math.pi / (-2))
    if x == 0 and y == 0:
        conor = 0
    r = round(r, 2)
    conor = round(conor, 2)
    return (r, conor)


if __name__ == '__main__':
    print("to polar")
    print(convert_cartesian_to_polar(1, 1))  # (1.41, 45.0)
    print(convert_cartesian_to_polar(0, 0))  # (0.0, 0.0)
    print(convert_cartesian_to_polar(0, 1))  # (1.0, 90.0)
    print(convert_cartesian_to_polar(-3, -4))  # (5.0, -126.87)

    print("\nto cartesian")
    print(convert_polar_to_cartesian(1, 90))  # (0.0, 1.0)
    print(convert_polar_to_cartesian(0, 0))  # (0.0, 0.0)
    print(convert_polar_to_cartesian(2, 60))  # (1.0, 1.73)
    print(convert_polar_to_cartesian(3, -40))  # (2.3, -1.93)
