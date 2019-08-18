from math import log10, sqrt

from weighting.constants import DB_GAIN_1KHZ, DB_GAIN_2KHZ


def r468(f, kHz):
    """Takes a frequency value and returns a weighted dB value.

    For weightening, the ITU-R BS.468-4 standard is followed.

    Parameters
    ----------
    f : float
        The frequency value must be a value from greater 0 to 96000.
    kHz : string
        Choose `1kHz` or `2kHz` as an weighting option (default `1kHz`).
        The weighting curves have the same shape for both options.
        They are shifted in a way, that the gain is 0 dB
        at the given frequency (`1kHz` or `2kHz`).

    Returns
    -------
    float
        The dB weighted value of the frequency.

    Raises
    ------
    ValueError
        If parameter f is not greater 0 and smaller or equal to 96000.
        If parameter is not equal to `1kHz` or `2kHz`.
    """

    if f > 0 and f <= 96000:
        pass
    else:
        raise ValueError

    f2, f3, f4, f5, f6 = f ** 2, f ** 3, f ** 4, f ** 5, f ** 6
    h1 = (
        (-4.7373389813783836e-24 * f6)
        + (2.0438283336061252e-15 * f4)
        - (1.363894795463638e-07 * f2)
        + 1
    )
    h2 = (
        (1.3066122574128241e-19 * f5)
        - (2.1181508875186556e-11 * f3)
        + (0.0005559488023498643 * f)
    )
    r_itu = (0.0001246332637532143 * f) / sqrt(h1 ** 2 + h2 ** 2)

    if kHz == "1kHz":
        gain = DB_GAIN_1KHZ
    elif kHz == "2kHz":
        gain = DB_GAIN_2KHZ
    else:
        raise ValueError

    return gain + 20 * log10(r_itu)
