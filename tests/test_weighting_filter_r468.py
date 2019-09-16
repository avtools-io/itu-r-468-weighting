from math import inf

import pytest

from itu_r_468_weighting.filter import r468

from .constants import GLOBAL_DB_TOLERANCE, ITU_R_468__FREQS_AND_EXP_VALS


@pytest.mark.parametrize(
    "start, end, khz_option, returns",
    [
        (1, 192000, "1khz", "db"),
        (1, 192000, "1khz", "factor"),
        (1, 192000, "2khz", "db"),
        (1, 192000, "2khz", "factor"),
    ],
)
def test_frequency_value_that_must_succeed(start, end, khz_option, returns):
    for i in range(start, end + 1):
        r468(i, khz_option, returns)


@pytest.mark.parametrize(
    "hz, khz_option, returns",
    [
        (-10, "1khz", "db"),
        (-10, "1khz", "factor"),
        (-10, "2khz", "db"),
        (-10, "2khz", "factor"),
    ],
)
def test_value_lt_0_that_must_raise_value_error(hz, khz_option, returns):
    with pytest.raises(ValueError):
        r468(hz, khz_option, returns)


@pytest.mark.parametrize(
    "hz, khz_option, returns",
    [
        (0, "1khz", "db"),
        (0, "1khz", "factor"),
        (0, "2khz", "db"),
        (0, "2khz", "factor"),
    ],
)
def test_value_of_0_that_must_return_inf(hz, khz_option, returns):
    assert r468(hz, khz_option, returns) == inf


@pytest.mark.parametrize(
    "khz_option, returns",
    [
        # wrong khz_option, correct "returns" parameter
        ("3khz", "db"),
        (1, "db"),
        (2.0, "db"),
        ("3khz", "factor"),
        (1, "factor"),
        (2.0, "factor"),
        # correct "khz_option", wrong "returns" parameter
        ("1khz", "wrong_string_value"),
        ("1khz", 123),
        ("1khz", 1.23),
        ("2khz", "wrong_string_value"),
        ("2khz", 123),
        ("2khz", 1.23),
    ],
)
def test_wrong_options_that_must_raise_value_error(khz_option, returns):
    with pytest.raises(ValueError):
        r468(1, khz_option, returns)


@pytest.mark.parametrize("f", ITU_R_468__FREQS_AND_EXP_VALS)
def test_r468__against_itu_r_468_1khz_value_specs(f):
    assert (
        abs(f.expected_db - r468(f.frequency_hz, f.khz_option, "db"))
        <= GLOBAL_DB_TOLERANCE
    )


@pytest.mark.parametrize("f", ITU_R_468__FREQS_AND_EXP_VALS)
def test_r468__against_itu_r_468_1khz_value_specs_tolerances(f):
    assert (
        round(f.expected_db - r468(f.frequency_hz, f.khz_option, "db"), 1)
        >= f.lower_tolerance
    )
    assert (
        round(f.expected_db - r468(f.frequency_hz, f.khz_option, "db"), 1)
        <= f.upper_tolerance
    )
