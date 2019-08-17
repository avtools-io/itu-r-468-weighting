from pytest import raises

from weighting.constants import (
    DB_TOLERANCE,
    ITU_R_468__FREQS_AND_EXP_VALS__1KHZ,
    ITU_R_468__FREQS_AND_EXP_VALS__2KHZ,
)
from weighting.filter import r468


def test_r468__frequency_values():
    for i in range(1, 96001):
        r468(i)
    for i in range(1, 96001):
        r468(i, "1kHz")
    for i in range(1, 96001):
        r468(i, "2kHz")


def test_r468__forbidden_values():
    with raises(ValueError):
        r468(-10)
    with raises(ValueError):
        r468(0)
    with raises(ValueError):
        r468(96001)


def test_r468__wrong_kHz_option():
    with raises(ValueError):
        r468(1, "3kHz")
    with raises(ValueError):
        r468(1, 1)
    with raises(ValueError):
        r468(1, 1.0)


def test_r468__against_itu_r_468_value_specs():
    for f in ITU_R_468__FREQS_AND_EXP_VALS__1KHZ:
        assert abs(f[1] - r468(f[0], "1kHz")) <= DB_TOLERANCE
    for f in ITU_R_468__FREQS_AND_EXP_VALS__2KHZ:
        assert abs(f[1] - r468(f[0], "2kHz")) <= DB_TOLERANCE
