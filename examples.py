from itu_r_468_weighting.filter import r468
from tests.constants import GLOBAL_DB_TOLERANCE, ITU_R_468__FREQS_AND_EXP_VALS

# Example usage:
if __name__ == "__main__":

    print("\nSimple usage examples:\n")
    print("r468(1000, '1khz', 'db'):", r468(1000, "1khz", "db"))
    print("r468(1000, '2khz', 'db'):", r468(1000, "2khz", "db"))
    print("r468(1000, '1khz', 'factor'):", r468(1000, "1khz", "factor"))
    print("r468(1000, '2khz', 'factor'):", r468(1000, "2khz", "factor"))

    print("\nWith '1khz' and returns 'db' options:\n")
    for f in ITU_R_468__FREQS_AND_EXP_VALS:
        if f.khz_option is "1khz":
            print(f.frequency_hz, r468(f.frequency_hz, "1khz", "db"))

    print("\nWith '2khz' and returns 'db' options:\n")
    for f in ITU_R_468__FREQS_AND_EXP_VALS:
        if f.khz_option is "2khz":
            print(f.frequency_hz, r468(f.frequency_hz, "2khz", "db"))

    print("\nWith '1khz' and returns 'factor' options:\n")
    for f in ITU_R_468__FREQS_AND_EXP_VALS:
        if f.khz_option is "1khz":
            print(f.frequency_hz, r468(f.frequency_hz, "1khz", "factor"))

    print("\nWith '2khz' and returns 'factor' options:\n")
    for f in ITU_R_468__FREQS_AND_EXP_VALS:
        if f.khz_option is "2khz":
            print(f.frequency_hz, r468(f.frequency_hz, "2khz", "factor"))

    print("\nFind max dB difference:\n")
    db_values = [
        abs(f.expected_db - r468(f.frequency_hz, f.khz_option, "db"))
        for f in ITU_R_468__FREQS_AND_EXP_VALS
    ]

    max_db = max(db_values)
    print("Max      :", max_db)
    print("Tolerance:", GLOBAL_DB_TOLERANCE)
    print("Value <= Tolerance?:", max_db <= GLOBAL_DB_TOLERANCE)

    # Run all integer values from 1 up to 192000 x times
    for _ in range(15):
        for i in range(1, 192001):
            r468(i, "1khz", "db")
