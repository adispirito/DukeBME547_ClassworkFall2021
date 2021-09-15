# def test_hdl_analysis_normal():
#     from blood_calculator import hdl_analysis
#     answer = hdl_analysis(65)
#     expected = "Normal"
#     assert answer == expected
# def test_hdl_analysis_borderline_low():
#     from blood_calculator import hdl_analysis
#     answer = hdl_analysis(50)
#     expected = "Borderline Low"
#     assert answer == expected
# def test_hdl_analysis_low():
#     from blood_calculator import hdl_analysis
#     answer = hdl_analysis(30)
#     expected = "Low"
#     assert answer == expected


import pytest


@pytest.mark.parametrize(
    "HDL_value, expected",
    [
        (65, "Normal"),
        (50, "Borderline Low"),
        (30, "Low")
    ],
)
def test_hdl_analysis(HDL_value, expected):
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(HDL_value)
    assert answer == expected
