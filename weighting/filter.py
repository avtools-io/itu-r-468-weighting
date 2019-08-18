from math import log10, sqrt

from weighting.constants import DB_GAIN_1KHZ, DB_GAIN_2KHZ


def r468(frequency_hz, khz_option):
    """Takes a frequency value and returns a weighted dB value.

    For weightening, the ITU-R BS.468-4 standard is followed.

    Parameters
    ----------
    frequency_hz : float
        The frequency value (in Hz) must be a value greater 0.
    khz_option : string
        Choose `1khz` or `2khz` as an weighting option (default `1khz`).
        The weighting curves have the same shape for both options.
        They are shifted in a way, that the gain is 0.0 dB
        at the given frequency (1 or 2 kHz).

    Returns
    -------
    float
        The dB weighted value of the frequency.

    Raises
    ------
    ValueError
        If parameter `frequency_hz` is not greater 0.
        If parameter `khz_option` is not equal to `1khz` or `2khz`.
    """

    if frequency_hz > 0:
        pass
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

    if khz_option == "1khz":
        gain = DB_GAIN_1KHZ
    elif khz_option == "2khz":
        gain = DB_GAIN_2KHZ
    else:
        raise ValueError

    return gain + 20 * log10(r_itu)
