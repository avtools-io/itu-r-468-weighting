# itu-r-468-weighting

A zero dependency Python ITU-R 468 noise weighting filter (1 kHz and 2 kHz)

Master branch: [![Build Status](https://travis-ci.com/cinelexi/itu-r-468-weighting.svg?branch=master)](https://travis-ci.com/cinelexi/itu-r-468-weighting?branch=master) [![Coverage Status](https://coveralls.io/repos/github/cinelexi/itu-r-468-weighting/badge.svg?branch=master)](https://coveralls.io/github/cinelexi/itu-r-468-weighting?branch=master) \
Dev branch: [![Build Status](https://travis-ci.com/cinelexi/itu-r-468-weighting.svg?branch=dev)](https://travis-ci.com/cinelexi/itu-r-468-weighting?branch=dev) [![Coverage Status](https://coveralls.io/repos/github/cinelexi/itu-r-468-weighting/badge.svg?branch=dev)](https://coveralls.io/github/cinelexi/itu-r-468-weighting?branch=dev)

## Introduction

This project consists of a sole function named `r468`. The function takes a frequency value and returns a weighted dB value. For weightening, the [ITU-R BS.468-4](https://www.itu.int/rec/R-REC-BS.468-4-198607-I/en) standard and the [SMPTE RP 2054:2010](https://ieeexplore.ieee.org/document/7290513) recommended practice are followed.

The math for this project is taken from Wikipedia (as of 2019-08-08):

- https://en.wikipedia.org/wiki/ITU-R_468_noise_weighting ([archived version](https://web.archive.org/web/20190808084536/https:/en.wikipedia.org/wiki/ITU-R_468_noise_weighting))

### Filter in dB:

![](images/filter_db.png)

### Filter amplification factor:

![](images/filter_amp_factor.png)

## Installation

```
pip install itu-r-468-weighting
```

More infos on the [project page](https://pypi.org/project/itu-r-468-weighting/) at PyPI.

## Example Usage

```
from itu_r_468_weighting.filter import r468

r468(1000, "1khz")
r468(1000, "2khz")
```

## Function Description

`r468(frequency_hz, khz_option)`

- Takes a frequency value and returns a weighted dB value.

### Parameters

`frequency_hz` : `float`

- The frequency value (in Hz) must be a value greater 0.

`khz_option` : `str`

- Choose `1khz` or `2khz` as an weighting option.
  The weighting curves have the same shape for both options.
  They are shifted in a way, that the gain is 0.0 dB
  at the given frequency (1 or 2 kHz).

### Returns

`float`

- The dB weighted value of the frequency.

### Raises

`ValueError`

- If parameter `frequency_hz` is not greater 0.
- If parameter `khz_option` is not equal to `1khz` or `2khz`.

## Developement

This project is hosted on [GitHub](https://github.com/cinelexi/itu-r-468-weighting).
