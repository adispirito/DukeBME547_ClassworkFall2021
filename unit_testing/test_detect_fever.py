import pytest


@pytest.mark.parametrize(
    "val, expected",
    [
        ([96, 96.5, 103.1, 98.7], True),
        ([96, 96.5, 97.1, 98.7], False),
    ],
)
def test_detect_fever(val, expected):
    from temp_calc import detect_fever
    answer = detect_fever(val)
    assert answer == expected
