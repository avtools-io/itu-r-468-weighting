from weighting.constants import (
    DB_TOLERANCE,
    ITU_R_468__FREQS,
    ITU_R_468__FREQS_AND_EXP_VALS__1KHZ,
    ITU_R_468__FREQS_AND_EXP_VALS__2KHZ,
)
from weighting.filter import r468

# Example usage:
if __name__ == "__main__":

    print("\nSimple usage examples:\n")
    print("r468(1000):", r468(1000))
    print("r468(1000, '1kHz'):", r468(1000, "1kHz"))
    print("r468(1000, '2kHz'):", r468(1000, "2kHz"))

    print("\nWith '1kHz' option:\n")
    for f in ITU_R_468__FREQS:
        print(f, r468(f, "1kHz"))

    print("\nWith '2kHz' option:\n")
    for f in ITU_R_468__FREQS:
        print(f, r468(f, "2kHz"))

    print("\nFind max dB difference with '1kHz' option:\n")
    db_values_1k = []

    for f in ITU_R_468__FREQS_AND_EXP_VALS__1KHZ:
        db_values_1k.append(abs(f[1] - r468(f[0], "1kHz")))

    max_1k = max(db_values_1k)
    print("Max      :", max_1k)
    print("Tolerance:", DB_TOLERANCE)
    print("Value <= Tolerance?:", max_1k <= DB_TOLERANCE)

    print("\nFind max dB difference with '2kHz' option:\n")
    db_values_2k = []
    for f in ITU_R_468__FREQS_AND_EXP_VALS__2KHZ:
        db_values_2k.append(abs(f[1] - r468(f[0], "2kHz")))

    max_2k = max(db_values_2k)
    print("Max      :", max_2k)
    print("Tolerance:", DB_TOLERANCE)
    print("Value <= Tolerance?:", max_2k <= DB_TOLERANCE)

    # Run all possible integer values
    for _ in range(30):
        for i in range(1, 96001):
            r468(i, "1kHz")
