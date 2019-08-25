import matplotlib.pyplot as plt

from itu_r_468_weighting.constants import (
    DB_TOLERANCE,
    ITU_R_468__FREQS,
    ITU_R_468__FREQS_AND_EXP_VALS__1KHZ,
    ITU_R_468__FREQS_AND_EXP_VALS__2KHZ,
)
from itu_r_468_weighting.filter import r468

# Example usage:
if __name__ == "__main__":

    print("\nSimple usage examples:\n")
    print("r468(1000, '1khz'):", r468(1000, "1khz"))
    print("r468(1000, '2khz'):", r468(1000, "2khz"))

    print("\nWith '1khz' option:\n")
    for f in ITU_R_468__FREQS:
        print(f, r468(f, "1khz"))

    print("\nWith '2khz' option:\n")
    for f in ITU_R_468__FREQS:
        print(f, r468(f, "2khz"))

    print("\nWith '1khz' and returns 'norm' options:\n")
    for f in ITU_R_468__FREQS:
        print(f, r468(f, "1khz", "norm"))

    print("\nWith '2khz' and returns 'norm' options:\n")
    for f in ITU_R_468__FREQS:
        print(f, r468(f, "2khz", "norm"))

    print("\nFind max dB difference with '1khz' option:\n")
    db_values_1k = []

    for f in ITU_R_468__FREQS_AND_EXP_VALS__1KHZ:
        db_values_1k.append(abs(f[1] - r468(f[0], "1khz")))

    max_1k = max(db_values_1k)
    print("Max      :", max_1k)
    print("Tolerance:", DB_TOLERANCE)
    print("Value <= Tolerance?:", max_1k <= DB_TOLERANCE)

    print("\nFind max dB difference with '2khz' option:\n")
    db_values_2k = []
    for f in ITU_R_468__FREQS_AND_EXP_VALS__2KHZ:
        db_values_2k.append(abs(f[1] - r468(f[0], "2khz")))

    max_2k = max(db_values_2k)
    print("Max      :", max_2k)
    print("Tolerance:", DB_TOLERANCE)
    print("Value <= Tolerance?:", max_2k <= DB_TOLERANCE)

    db_1k = []
    for i in range(24001):
        db_1k.append(r468(i, "1khz"))

    db_2k = []
    for i in range(24001):
        db_2k.append(r468(i, "2khz"))

    plt.plot(db_1k)
    plt.plot(db_2k)
    plt.xscale("symlog", linthreshy=0.015)
    plt.grid(True)
    plt.ylabel("dB")
    plt.axis([10, 100e3, -50, 20])
    plt.show()

    db_1k_norm = []
    for i in range(24001):
        db_1k_norm.append(r468(i, "1khz", "norm"))

    db_2k_norm = []
    for i in range(24001):
        db_2k_norm.append(r468(i, "2khz", "norm"))

    plt.plot(db_1k_norm)
    plt.plot(db_2k_norm)
    plt.ylabel("normalized")
    plt.show()

    # # Run all integer values from 1 up to 192000 x times
    # for _ in range(15):
    #     for i in range(1, 192001):
    #         r468(i, "1khz")
