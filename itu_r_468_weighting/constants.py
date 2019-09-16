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

# Gain factor, "1khz" option
FACTOR_GAIN_1KHZ = 10 ** (DB_GAIN_1KHZ / 20)

# Gain factor, "2khz" option
FACTOR_GAIN_2KHZ = 10 ** (DB_GAIN_2KHZ / 20)
