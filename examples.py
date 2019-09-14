from itu_r_468_weighting.constants import (
    GLOBAL_DB_TOLERANCE,
    ITU_R_468__FREQS_AND_EXP_VALS__1KHZ,
    ITU_R_468__FREQS_AND_EXP_VALS__2KHZ,
)
from itu_r_468_weighting.filter import r468

ITU_R_468__FREQS = [f[0] for f in ITU_R_468__FREQS_AND_EXP_VALS__1KHZ]

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
    print("Tolerance:", GLOBAL_DB_TOLERANCE)
    print("Value <= Tolerance?:", max_1k <= GLOBAL_DB_TOLERANCE)

    print("\nFind max dB difference with '2khz' option:\n")
    db_values_2k = []
    for f in ITU_R_468__FREQS_AND_EXP_VALS__2KHZ:
        db_values_2k.append(abs(f[1] - r468(f[0], "2khz")))

    max_2k = max(db_values_2k)
    print("Max      :", max_2k)
    print("Tolerance:", GLOBAL_DB_TOLERANCE)
    print("Value <= Tolerance?:", max_2k <= GLOBAL_DB_TOLERANCE)

    # Run all integer values from 1 up to 192000 x times
    for _ in range(15):
        for i in range(1, 192001):
            r468(i, "1khz")
