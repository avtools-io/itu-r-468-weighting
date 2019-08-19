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
# option result) to the constant value of DB_GAIN_1KHZ:
# DB_GAIN_2KHZ = DB_GAIN_1KHZ - r468(2000, "1khz") + r468(1000, "1khz")
DB_GAIN_2KHZ = 12.617052124255618

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
    [31.5, -29.9],
    [63, -23.9],
    [100, -19.8],
    [200, -13.8],
    [400, -7.8],
    [800, -1.9],
    [1000, 0.0],
    [2000, 5.6],
    [3150, 9.0],
    [4000, 10.5],
    [5000, 11.7],
    [6300, 12.2],
    [7100, 12.0],
    [8000, 11.4],
    [9000, 10.1],
    [10000, 8.1],
    [12500, 0.0],
    [14000, -5.3],
    [16000, -11.7],
    [20000, -22.2],
    [31500, -42.7],
]

ITU_R_468__FREQS_AND_EXP_VALS__2KHZ = [
    # [<frequency in Hz>, <expected value in dB>],
    [31.5, -35.5],
    [63, -29.5],
    [100, -25.4],
    [200, -19.4],
    [400, -13.4],
    [800, -7.5],
    [1000, -5.6],
    [2000, 0.0],
    [3150, 3.4],
    [4000, 4.9],
    [5000, 6.1],
    [6300, 6.6],
    [7100, 6.4],
    [8000, 5.8],
    [9000, 4.5],
    [10000, 2.5],
    [12500, -5.6],
    [14000, -10.9],
    [16000, -17.3],
    [20000, -27.8],
    [31500, -48.3],
]
