from math import inf

# DB_TOLERANCE was determined by taking the maximum value of the difference
# between computed ("1khz" and "2khz" option) and expected ITU-R 468 values.
# If the r468 function improves over time, this constant should converge to 0.
DB_TOLERANCE = 0.07184434988229427

# DB_GAIN_1KHZ was first determined with the multiplication factor of 8.1333
# (+18.20533583440004 dB). From there on the value was modified to find
# a better one, by converging the distance to 0 at 1000 Hz and 12500 Hz, having
# the same value for both: r468(1000, "1khz") == r468(12500, "1khz")
DB_GAIN_1KHZ = 18.246265068039158

# DB_GAIN_2KHZ was determined by substracting the dB value at 2000 Hz (of
# the "1khz" option result) from and adding the value at 1000 Hz (of the "1khz"
# option result) to the value of DB_GAIN_1KHZ:
# DB_GAIN_2KHZ = DB_GAIN_1KHZ - r468(2000, "1khz") + r468(1000, "1khz")
DB_GAIN_2KHZ = 12.617052124255618

NORM_GAIN_1KHZ = 10 ** (DB_GAIN_1KHZ / 20)
NORM_GAIN_2KHZ = 10 ** (DB_GAIN_2KHZ / 20)

ITU_R_468__FREQS = [
    # <frequency in Hz>,
    31.5,
    63,
    100,
    200,
    400,
    800,
    1000,
    2000,
    3150,
    4000,
    5000,
    6300,
    7100,
    8000,
    9000,
    10000,
    12500,
    14000,
    16000,
    20000,
    31500,
]

ITU_R_468__FREQS_AND_EXP_VALS__1KHZ = [
    # [<frequency in Hz>, <expected value in dB>],
    [31.5, -29.9, [-2.0, 2.0]],
    [63, -23.9, [-1.4, 1.4]],
    [100, -19.8, [-1.0, 1.0]],
    [200, -13.8, [-0.85, 0.85]],
    [400, -7.8, [-0.7, 0.7]],
    [800, -1.9, [-0.55, 0.55]],
    [1000, 0.0, [-0.5, 0.5]],
    [2000, 5.6, [-0.5, 0.5]],
    [3150, 9.0, [-0.5, 0.5]],
    [4000, 10.5, [-0.5, 0.5]],
    [5000, 11.7, [-0.5, 0.5]],
    [6300, 12.2, [0.0, 0.0]],
    [7100, 12.0, [-0.2, 0.2]],
    [8000, 11.4, [-0.4, 0.4]],
    [9000, 10.1, [-0.6, 0.6]],
    [10000, 8.1, [-0.8, 0.8]],
    [12500, 0.0, [-1.2, 1.2]],
    [14000, -5.3, [-1.4, 1.4]],
    [16000, -11.7, [-1.6, 1.6]],
    [20000, -22.2, [-2.0, 2.0]],
    [31500, -42.7, [-inf, 2.8]],
]

ITU_R_468__FREQS_AND_EXP_VALS__2KHZ = [
    # [<frequency in Hz>, <expected value in dB>],
    # Revert 31 to 31.5 Hz, assume mistake in SMPTE RP
    [31.5, -35.5, [-2.0, 2.0]],
    [63, -29.5, [-1.4, 1.4]],
    [100, -25.4, [-1.0, 1.0]],
    [200, -19.4, [-0.85, 0.85]],
    [400, -13.4, [-0.7, 0.7]],
    [800, -7.5, [-0.55, 0.55]],
    [1000, -5.6, [-0.5, 0.5]],
    [2000, 0.0, [-0.5, 0.5]],
    [3150, 3.4, [-0.5, 0.5]],
    [4000, 4.9, [-0.5, 0.5]],
    [5000, 6.1, [-0.5, 0.5]],
    [6300, 6.6, [0.0, 0.0]],
    [7100, 6.4, [-0.2, 0.2]],
    [8000, 5.8, [-0.4, 0.4]],
    [9000, 4.5, [-0.6, 0.6]],
    [10000, 2.5, [-0.8, 0.8]],
    [12500, -5.6, [-1.2, 1.2]],
    [14000, -10.9, [-1.4, 1.4]],
    [16000, -17.3, [-1.65, 1.65]],
    [20000, -27.8, [-2.0, 2.0]],
    [31500, -48.3, [-inf, 2.8]],
]
