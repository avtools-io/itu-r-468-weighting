from math import log10, sqrt

from itu_r_468_weighting.constants import (
    DB_GAIN_1KHZ,
    DB_GAIN_2KHZ,
    NORM_GAIN_1KHZ,
    NORM_GAIN_2KHZ,
)


def r468(frequency_hz, khz_option, returns="db"):
    """Takes a frequency value and returns a weighted gain value.

    For weightening, the ITU-R BS.468-4 standard and the
    SMPTE RP 2054:2010 recommended practice are followed.

    Parameters
    ----------
    frequency_hz : float
        The frequency value (in Hz) must be a value greater 0.
    khz_option : str
        Choose `1khz` or `2khz` as an weighting option.
        The weighting curves have a similar characteristic for both options,
        but are using a different amplification factor.
        They are shifted in a way, that the gain is 0.0 dB
        at the given frequency (1 or 2 kHz).
    returns : str
        Choose `db` or `norm` as option. `db` will output the
        weighted gain value in dB. `norm` will output the weighted
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
        return float("-inf")
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

    if returns == "db":
        r_itu = (0.0001246332637532143 * f1) / sqrt(h1 ** 2 + h2 ** 2)
        if khz_option == "1khz":
            gain = DB_GAIN_1KHZ
            return gain + 20 * log10(r_itu)
        elif khz_option == "2khz":
            gain = DB_GAIN_2KHZ
            return gain + 20 * log10(r_itu)
        else:
            raise ValueError
    elif returns == "norm":
        if khz_option == "1khz":
            gain = NORM_GAIN_1KHZ
            return gain * 0.0001246332637532143 * f1 / sqrt(h1 ** 2 + h2 ** 2)
        elif khz_option == "2khz":
            gain = NORM_GAIN_2KHZ
            return gain * 0.0001246332637532143 * f1 / sqrt(h1 ** 2 + h2 ** 2)
        else:
            raise ValueError
    else:
        raise ValueError
