import pytest

from itu_r_468_weighting.constants import (
    DB_TOLERANCE,
    ITU_R_468__FREQS_AND_EXP_VALS__1KHZ,
    ITU_R_468__FREQS_AND_EXP_VALS__2KHZ,
)
from itu_r_468_weighting.filter import r468


@pytest.mark.parametrize(
    "start, end, khz_option", [(1, 192000, "1khz"), (1, 192000, "2khz")]
)
def test_frequency_value_that_must_succeed(start, end, khz_option):
    for i in range(start, end + 1):
        r468(i, khz_option)


@pytest.mark.parametrize(
    "hz, khz_option", [(-10, "1khz"), (0, "1khz"), (-10, "2khz"), (0, "2khz")]
)
def test_value_less_or_equal_to_0_that_must_raise_value_error(hz, khz_option):
    with pytest.raises(ValueError):
        r468(hz, khz_option)


@pytest.mark.parametrize("khz_option", ["3khz", 1, 2.0])
def test_wrong_khz_option_that_must_raise_value_error(khz_option):
    with pytest.raises(ValueError):
        r468(1, khz_option)


@pytest.mark.parametrize(
    "freqs, khz_option",
    [
        (ITU_R_468__FREQS_AND_EXP_VALS__1KHZ, "1khz"),
        (ITU_R_468__FREQS_AND_EXP_VALS__2KHZ, "2khz"),
    ],
)
def test_r468__against_itu_r_468_value_specs(freqs, khz_option):
    for f in freqs:
        assert abs(f[1] - r468(f[0], khz_option)) <= DB_TOLERANCE
