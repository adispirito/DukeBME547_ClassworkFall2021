from typing import Union


def find_y_for_x_on_line(plane_coord: tuple, x: Union[int, float]):
    point_0 = plane_coord[0]
    point_1 = plane_coord[1]
    m = find_slope(point_0, point_1)
    x0 = point_0[0]
    y0 = point_0[1]
    b = find_b(x0, y0, m)
    y = line_equation(x, m, b)
    return y


def find_slope(p0: tuple, p1: tuple):
    x0 = p0[0]
    y0 = p0[1]
    x1 = p1[0]
    y1 = p1[1]
    m = (y1 - y0)/(x1 - x0)
    return m


def find_b(x0: Union[int, float], y0: Union[int, float], m: Union[int, float]):
    b = y0 - x0 * m
    return b


def line_equation(x: Union[int, float],
                  m: Union[int, float],
                  b: Union[int, float]):
    y = m * x + b
    return y
