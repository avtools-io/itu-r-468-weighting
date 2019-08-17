from math import log10, sqrt


def r468(f, kHz='1kHz'):
    """Takes a frequency value and returns a weighted dB value.

    For weightening, the ITU-R-468 standard is followed.

    The math for this is taken from Wikipedia (as of 2019-08-08):

    https://en.wikipedia.org/wiki/ITU-R_468_noise_weighting

    Shortened link to the archived Wikipedia page (as of 2019-08-08):

    https://bit.ly/2P29qOh

    Parameters
    ----------
    f : float
        Frequency values should be values from 1 to 96000.
    kHz : string
        Choose '1kHz' or '2kHz' filtering (default '1kHz').

    Returns
    -------
    float
        The dB weighted value of the frequency.
    """

    f2, f3, f4, f5, f6 = f**2, f**3, f**4, f**5, f**6
    h1_1, h1_2, h1_3 = -4.737338981378384, 2.043828333606125, 1.363894795463638
    h1 = h1_1*(10**-24)*f6 + h1_2*(10**-15)*f4 - h1_3*(10**-7)*f2 + 1
    h2_1, h2_2, h2_3 = 1.306612257412824, 2.118150887518656, 5.559488023498642
    h2 = h2_1*(10**-19)*f5 - h2_2*(10**-11)*f3 + h2_3*(10**-4)*f
    rITU = (1.246332637532143*(10**-4)*f) / sqrt(h1**2 + h2**2)

    if kHz == '1kHz':
        gain = 18.2
    elif kHz == '2kHz':
        gain = 12.6
    else:
        raise ValueError

    return gain + 20 * log10(rITU)


if __name__ == '__main__':
    from frequencies import ITU_R_468_FREQUENCIES

    # Example usage:

    print('\nAt 1 kHz:\n')
    for f in ITU_R_468_FREQUENCIES:
        print(round(r468(f, '1kHz'), 1))

    print('\nAt 2 kHz:\n')
    for f in ITU_R_468_FREQUENCIES:
        print(round(r468(f, '2kHz'), 1))

    for i in range(1, 48001):
        r468(i, '1kHz')
