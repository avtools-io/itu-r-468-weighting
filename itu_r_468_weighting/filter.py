from math import inf, log10, sqrt
from typing import Union

from itu_r_468_weighting.constants import (
    DB_GAIN_1KHZ,
    DB_GAIN_2KHZ,
    FACTOR_GAIN_1KHZ,
    FACTOR_GAIN_2KHZ,
)


def r468(frequency_hz: Union[int, float], khz_option: str, returns: str) -> float:
    """Takes a frequency value and returns a weighted gain value.

    For weightening, the ITU-R BS.468-4 standard and the
    SMPTE RP 2054:2010 recommended practice are followed.

    Parameters
    ----------
    frequency_hz : int or float
        The frequency value (in Hz) must be a value greater 0.
    khz_option : str
        Choose `1khz` or `2khz` as an weighting option.
        The weighting curves have a similar characteristic for both options,
        but are using a different amplification factor.
        They are shifted in a way, that the gain is 0.0 dB
        at the given frequency (1 or 2 kHz).
    returns : str
        Choose `db` or `factor` as option. `db` will output the
        weighted gain value in dB. `factor` will output the weighted
        gain value as a factor.

    Returns
    -------
    float
        The weighted value of the frequency.

    Raises
    ------
    ValueError
        If parameter `frequency_hz` is not greater 0.
        If parameter `khz_option` is not equal to `1khz` or `2khz`.
    """

    if frequency_hz > 0:
        pass
    elif frequency_hz == 0:
        return inf
    else:
        raise ValueError

    f1, f2, f3, f4, f5, f6 = (
        frequency_hz,
        frequency_hz ** 2,
        frequency_hz ** 3,
        frequency_hz ** 4,
        frequency_hz ** 5,
        frequency_hz ** 6,
    )
    h1 = (
        (-4.7373389813783836e-24 * f6)
        + (2.0438283336061252e-15 * f4)
        - (1.363894795463638e-07 * f2)
        + 1
    )
    h2 = (
        (1.3066122574128241e-19 * f5)
        - (2.1181508875186556e-11 * f3)
        + (0.0005559488023498643 * f1)
    )
    r_itu = (0.0001246332637532143 * f1) / sqrt(h1 ** 2 + h2 ** 2)

    if returns == "db":
        if khz_option == "1khz":
            return DB_GAIN_1KHZ + 20 * log10(r_itu)
        elif khz_option == "2khz":
            return DB_GAIN_2KHZ + 20 * log10(r_itu)
        else:
            raise ValueError
    elif returns == "factor":
        if khz_option == "1khz":
            return FACTOR_GAIN_1KHZ * r_itu
        elif khz_option == "2khz":
            return FACTOR_GAIN_2KHZ * r_itu
        else:
            raise ValueError
    else:
        raise ValueError
