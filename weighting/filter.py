from math import log10, sqrt

from frequencies import ITU_R_468_FREQUENCIES


def r468(f, kHz=1):
    f2 = f**2
    f4 = f**4
    f6 = f**6
    h1_1 = -4.737338981378384
    h1_2 = 2.043828333606125
    h1_3 = 1.363894795463638
    h1 = h1_1 * (10**-24) * f6 + h1_2 * (10**-15) * \
        f4 - h1_3 * (10**-7) * f2 + 1
    f3 = f**3
    f5 = f**5
    h2_1 = 1.306612257412824
    h2_2 = 2.118150887518656
    h2_3 = 5.559488023498642
    h2 = h2_1 * (10**-19) * f5 - h2_2 * (10**-11) * f3 + h2_3 * (10**-4) * f
    rITU = (1.246332637532143 * (10**-4) * f) / sqrt(h1**2 + h2**2)
    if kHz == 1:
        gain = 18.2
    elif kHz == 2:
        gain = 12.6
    else:
        raise ValueError
    return gain + 20 * log10(rITU)


if __name__ == '__main__':

    print('\nAt 1 kHz:\n')
    for f in ITU_R_468_FREQUENCIES:
        print(round(r468(f, 1), 1))

    print('\nAt 2 kHz:\n')
    for f in ITU_R_468_FREQUENCIES:
        print(round(r468(f, 2), 1))
