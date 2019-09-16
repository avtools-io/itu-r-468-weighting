from itu_r_468_weighting.filter import r468
from tests.constants import GLOBAL_DB_TOLERANCE, ITU_R_468__FREQS_AND_EXP_VALS

# Example usage:
if __name__ == "__main__":

    print("\nSimple usage examples:\n")
    print("r468(1000, '1khz'):", r468(1000, "1khz"))
    print("r468(1000, '2khz'):", r468(1000, "2khz"))

    print("\nWith '1khz' option:\n")
    for f in ITU_R_468__FREQS_AND_EXP_VALS:
        if f.khz_option is "1khz":
            print(f.frequency, r468(f.frequency, "1khz"))

    print("\nWith '2khz' option:\n")
    for f in ITU_R_468__FREQS_AND_EXP_VALS:
        if f.khz_option is "2khz":
            print(f.frequency, r468(f.frequency, "2khz"))

    print("\nWith '1khz' and returns 'factor' options:\n")
    for f in ITU_R_468__FREQS_AND_EXP_VALS:
        if f.khz_option is "1khz":
            print(f.frequency, r468(f.frequency, "1khz", "factor"))

    print("\nWith '2khz' and returns 'factor' options:\n")
    for f in ITU_R_468__FREQS_AND_EXP_VALS:
        if f.khz_option is "2khz":
            print(f.frequency, r468(f.frequency, "2khz", "factor"))

    print("\nFind max dB difference:\n")
    db_values = [
        abs(f.expected_db - r468(f.frequency, f.khz_option))
        for f in ITU_R_468__FREQS_AND_EXP_VALS
    ]

    max_db = max(db_values)
    print("Max      :", max_db)
    print("Tolerance:", GLOBAL_DB_TOLERANCE)
    print("Value <= Tolerance?:", max_db <= GLOBAL_DB_TOLERANCE)

    # Run all integer values from 1 up to 192000 x times
    for _ in range(15):
        for i in range(1, 192001):
            r468(i, "1khz")
