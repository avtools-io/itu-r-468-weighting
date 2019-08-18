import pytest

from weighting.constants import (
    DB_TOLERANCE,
    ITU_R_468__FREQS_AND_EXP_VALS__1KHZ,
    ITU_R_468__FREQS_AND_EXP_VALS__2KHZ,
)
from weighting.filter import r468


@pytest.mark.parametrize(
    "start, end, khz_option", [(1, 192000, "1kHz"), (1, 192000, "2kHz")]
)
def test_frequency_value_that_must_succeed(start, end, khz_option):
    for i in range(start, end + 1):
        r468(i, khz_option)


@pytest.mark.parametrize(
    "hz, khz_option", [(-10, "1kHz"), (0, "1kHz"), (-10, "2kHz"), (0, "2kHz")]
)
def test_value_less_or_equal_to_0_that_must_raise_value_error(hz, khz_option):
    with pytest.raises(ValueError):
        r468(hz, khz_option)


@pytest.mark.parametrize("khz_option", ["3kHz", 1, 2.0])
def test_wrong_khz_option_that_must_raise_value_error(khz_option):
    with pytest.raises(ValueError):
        r468(1, khz_option)


@pytest.mark.parametrize(
    "freqs, khz_option",
    [
        (ITU_R_468__FREQS_AND_EXP_VALS__1KHZ, "1kHz"),
        (ITU_R_468__FREQS_AND_EXP_VALS__2KHZ, "2kHz"),
    ],
)
def test_r468__against_itu_r_468_value_specs(freqs, khz_option):
    for f in freqs:
        assert abs(f[1] - r468(f[0], khz_option)) <= DB_TOLERANCE
