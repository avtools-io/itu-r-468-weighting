from pytest import raises

from weighting.filter import r468
from weighting.frequencies import ITU_R_468_FREQS_AND_EXPECTED_VALUES


def test_r468__frequency_values():
    for i in range(1, 96001):
        r468(i)
    for i in range(1, 96001):
        r468(i, '1kHz')
    for i in range(1, 96001):
        r468(i, '2kHz')


def test_r468__forbidden_values():
    with raises(ValueError):
        r468(-10)
    with raises(ValueError):
        r468(0)
    with raises(ValueError):
        r468(96001)


def test_r468__wrong_kHz_option():
    with raises(ValueError):
        r468(1, '3kHz')
    with raises(ValueError):
        r468(1, 1)
    with raises(ValueError):
        r468(1, 1.0)


def test_r468__against_itu_r_468_value_specs():
    db_tolerance = 0.08889647413791124
    for f in ITU_R_468_FREQS_AND_EXPECTED_VALUES:
        assert abs(f[1] - r468(f[0])) <= db_tolerance
