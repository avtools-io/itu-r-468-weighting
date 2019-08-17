DB_TOLERANCE = 0.08356063973787187
# DB_GAIN_1KHZ was determined with factor 8.1333
DB_GAIN_1KHZ = 18.20533583440004
# DB_GAIN_2KHZ was determined by subtracting the 2 kHz from the 1 kHz dB gain
# values of the r468 function with '1kHz' option and then subctracting the
# result from the DB_GAIN_1KHZ value
DB_GAIN_2KHZ = 12.5761228906165


ITU_R_468_FREQS_AND_EXPECTED_VALUES = [
    # [<frequency in Hz>, <expected value in dB>]
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
    [12500,	0.0],
    [14000,	-5.3],
    [16000,	-11.7],
    [20000,	-22.2],
    [31500,	-42.7]
]
