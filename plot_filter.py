import matplotlib.pyplot as plt

from itu_r_468_weighting.filter import r468

if __name__ == "__main__":

    db_1k = []
    for i in range(24001):
        db_1k.append(r468(i, "1khz"))

    db_2k = []
    for i in range(24001):
        db_2k.append(r468(i, "2khz"))

    plt.plot(db_1k, "-b", label="1 kHz")
    plt.plot(db_2k, "-r", label="2 kHz")
    plt.legend(loc="upper left")
    plt.xscale("symlog", linthreshy=0.015)
    plt.grid(True)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Gain (dB)")
    plt.axis([10, 100e3, -50, 20])
    plt.show()

    db_1k_norm = []
    for i in range(24001):
        db_1k_norm.append(r468(i, "1khz", "norm"))

    db_2k_norm = []
    for i in range(24001):
        db_2k_norm.append(r468(i, "2khz", "norm"))

    plt.plot(db_1k_norm, "-b", label="1 kHz")
    plt.plot(db_2k_norm, "-r", label="2 kHz")
    plt.legend(loc="upper left")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Gain")
    plt.show()
