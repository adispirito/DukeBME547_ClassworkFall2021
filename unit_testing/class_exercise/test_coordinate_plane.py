import pytest


@pytest.mark.parametrize(
    "plane_coord, x, expected",
    [
        (((0, 1), (1, 0)), 0, 1),
        (((0, 1), (1, 0)), 1, 0),
        (((0, 1), (1, 0)), 0.5, 0.5),
    ],
)
def test_coordinate_plane_find_y_for_x_on_line(plane_coord, x, expected):
    from coordinate_plane import find_y_for_x_on_line
    answer = find_y_for_x_on_line(plane_coord, x)
    assert answer == expected


@pytest.mark.parametrize(
    "p0, p1, expected",
    [
        ((0, 1), (1, 0), -1),
        ((0, 0), (1, 1), 1),
        ((0, 0), (1, 2), 2),
    ],
)
def test_coordinate_plane_find_slope(p0, p1, expected):
    from coordinate_plane import find_slope
    answer = find_slope(p0, p1)
    assert answer == expected


@pytest.mark.parametrize(
    "x0, y0, m, expected",
    [
        (0, 0, 1, 0),
        (2, 2, 2, -2),
        (2, 5, 4, -3),
    ],
)
def test_coordinate_plane_find_b(x0, y0, m, expected):
    from coordinate_plane import find_b
    answer = find_b(x0, y0, m)
    assert answer == expected


@pytest.mark.parametrize(
    "x, m, b, expected",
    [
        (0, 1, 0, 0),
        (3, 4, -3, 9),
        (3, 7, -20, 1),
    ],
)
def test_coordinate_plane_line_equation(x, m, b, expected):
    from coordinate_plane import line_equation
    answer = line_equation(x, m, b)
    assert answer == expected
