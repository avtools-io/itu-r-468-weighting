# py-itu-r-468-weighting

A zero dependency Python ITU-R 468 noise weighting filter (1 and 2 kHz)

Master branch: [![Build Status](https://travis-ci.com/cinelexi/py-itu-r-468-weighting.svg?branch=master)](https://travis-ci.com/cinelexi/py-itu-r-468-weighting?branch=master) [![Coverage Status](https://coveralls.io/repos/github/cinelexi/py-itu-r-468-weighting/badge.svg?branch=master)](https://coveralls.io/github/cinelexi/py-itu-r-468-weighting?branch=master) \
Dev branch: [![Build Status](https://travis-ci.com/cinelexi/py-itu-r-468-weighting.svg?branch=dev)](https://travis-ci.com/cinelexi/py-itu-r-468-weighting?branch=dev) [![Coverage Status](https://coveralls.io/repos/github/cinelexi/py-itu-r-468-weighting/badge.svg?branch=dev)](https://coveralls.io/github/cinelexi/py-itu-r-468-weighting?branch=dev)

## Introduction

This project consists of a sole function named `r468`. The function takes a frequency value and returns a weighted dB value. For weightening, the [ITU-R BS.468-4](https://www.itu.int/rec/R-REC-BS.468-4-198607-I/en) standard and the [SMPTE RP 2054:2010](https://ieeexplore.ieee.org/document/7290513) recommended practice are followed.

The math for this project is taken from Wikipedia (as of 2019-08-08):

- https://en.wikipedia.org/wiki/ITU-R_468_noise_weighting ([archived version](https://web.archive.org/web/20190808084536/https:/en.wikipedia.org/wiki/ITU-R_468_noise_weighting))

## Function Description

Can be found in the docstring of the function and on [GitHub](https://github.com/cinelexi/py-itu-r-468-weighting/blob/dev/weighting/filter.py).

## Installation

```
pip install itu_r_468_weighting
```

## Example Usage

```
from itu_r_468_weighting.filter import r468

r468(2000, "1khz")
```
