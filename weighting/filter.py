from math import log10, sqrt

from frequencies import ITU_R_468_FREQUENCIES


def r468(f):
    f2 = f**2
    f4 = f**4
    f6 = f**6
    h11 = -4.737338981378384
    h12 = 2.043828333606125
    h13 = 1.363894795463638
    h1 = h11 * (10**-24) * f6 + h12 * (10**-15) * f4 - h13 * (10**-7) * f2 + 1
    f3 = f**3
    f5 = f**5
    h21 = 1.306612257412824
    h22 = 2.118150887518656
    h23 = 5.559488023498642
    h2 = h21 * (10**-19) * f5 - h22 * (10**-11) * f3 + h23 * (10**-4) * f
    rITU = (1.246332637532143 * (10**-4) * f) / sqrt(h1**2 + h2**2)
    return 18.2 + 20 * log10(rITU)


if __name__ == '__main__':
    for f in ITU_R_468_FREQUENCIES:
        print(round(r468(f), 1))
