import pytest
from math import inf

from itu_r_468_weighting.constants import (
    GLOBAL_DB_TOLERANCE,
    ITU_R_468__FREQS_AND_EXP_VALS__1KHZ,
    ITU_R_468__FREQS_AND_EXP_VALS__2KHZ,
)
from itu_r_468_weighting.filter import r468


@pytest.mark.parametrize(
    "start, end, khz_option, returns",
    [
        (1, 192000, "1khz", None),
        (1, 192000, "1khz", "db"),
        (1, 192000, "1khz", "norm"),
        (1, 192000, "2khz", None),
        (1, 192000, "2khz", "db"),
        (1, 192000, "2khz", "norm"),
    ],
)
def test_frequency_value_that_must_succeed(start, end, khz_option, returns):
    if returns is None:
        for i in range(start, end + 1):
            r468(i, khz_option)
    else:
        for i in range(start, end + 1):
            r468(i, khz_option, returns)


@pytest.mark.parametrize(
    "hz, khz_option, returns",
    [
        (-10, "1khz", None),
        (-10, "1khz", "db"),
        (-10, "1khz", "norm"),
        (-10, "2khz", None),
        (-10, "2khz", "db"),
        (-10, "2khz", "norm"),
    ],
)
def test_value_lt_0_that_must_raise_value_error(hz, khz_option, returns):
    if returns is None:
        with pytest.raises(ValueError):
            r468(hz, khz_option)
    else:
        with pytest.raises(ValueError):
            r468(hz, khz_option, returns)


@pytest.mark.parametrize(
    "hz, khz_option, returns",
    [
        (0, "1khz", None),
        (0, "1khz", "db"),
        (0, "1khz", "norm"),
        (0, "2khz", None),
        (0, "2khz", "db"),
        (0, "2khz", "norm"),
    ],
)
def test_value_of_0_that_must_return_inf(hz, khz_option, returns):
    if returns is None:
        assert r468(hz, khz_option) == inf
    else:
        assert r468(hz, khz_option, returns) == inf


@pytest.mark.parametrize("khz_option", ["3khz", 1, 2.0])
def test_wrong_khz_option_that_must_raise_value_error(khz_option):
    with pytest.raises(ValueError):
        r468(1, khz_option)


@pytest.mark.parametrize(
    "freqs", [freqs for freqs in ITU_R_468__FREQS_AND_EXP_VALS__1KHZ]
)
def test_r468__against_itu_r_468_1khz_value_specs(freqs):
    assert abs(freqs[1] - r468(freqs[0], "1khz")) <= GLOBAL_DB_TOLERANCE


@pytest.mark.parametrize(
    "freqs", [freqs for freqs in ITU_R_468__FREQS_AND_EXP_VALS__1KHZ]
)
def test_r468__against_itu_r_468_1khz_value_specs_tolerances(freqs):
    assert round(freqs[1] - r468(freqs[0], "1khz"), 1) >= freqs[2][0]
    assert round(freqs[1] - r468(freqs[0], "1khz"), 1) <= freqs[2][1]


@pytest.mark.parametrize(
    "freqs", [freqs for freqs in ITU_R_468__FREQS_AND_EXP_VALS__2KHZ]
)
def test_r468__against_itu_r_468_2khz_value_specs(freqs):
    assert abs(freqs[1] - r468(freqs[0], "2khz")) <= GLOBAL_DB_TOLERANCE


@pytest.mark.parametrize(
    "freqs", [freqs for freqs in ITU_R_468__FREQS_AND_EXP_VALS__2KHZ]
)
def test_r468__against_itu_r_468_2khz_value_specs_tolerances(freqs):
    assert round(freqs[1] - r468(freqs[0], "2khz"), 1) >= freqs[2][0]
    assert round(freqs[1] - r468(freqs[0], "2khz"), 1) <= freqs[2][1]
