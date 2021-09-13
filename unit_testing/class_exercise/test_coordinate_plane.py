import pytest


@pytest.mark.parametrize(
    "plane_coord, x, expected",
    [
        (((0, 1), (1, 0)), 0, 1),
        (((0, 1), (1, 0)), 1, 0),
        (((0, 1), (1, 0)), 0.5, 0.5),
    ],
)
def test_coordinate_plane(plane_coord, x, expected):
    from coordinate_plane import find_y_for_x_on_line
    answer = find_y_for_x_on_line(plane_coord, x)
    assert answer == expected
