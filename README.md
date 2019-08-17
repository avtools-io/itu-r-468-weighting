# py-itu-r-468-weighting

Python ITU-R 468 noise weighting filter (1 and 2 kHz)

Master branch: [![Build Status](https://travis-ci.com/cinelexi/py-itu-r-468-weighting.svg?branch=master)](https://travis-ci.com/cinelexi/py-itu-r-468-weighting?branch=master) [![Coverage Status](https://coveralls.io/repos/github/cinelexi/py-itu-r-468-weighting/badge.svg?branch=master)](https://coveralls.io/github/cinelexi/py-itu-r-468-weighting?branch=master) \
Dev branch: [![Build Status](https://travis-ci.com/cinelexi/py-itu-r-468-weighting.svg?branch=dev)](https://travis-ci.com/cinelexi/py-itu-r-468-weighting?branch=dev) [![Coverage Status](https://coveralls.io/repos/github/cinelexi/py-itu-r-468-weighting/badge.svg?branch=dev)](https://coveralls.io/github/cinelexi/py-itu-r-468-weighting?branch=dev)

## Introduction

This projects consists of a sole function named `r468`. Which can be found in `weighting/filter.py`.

The function `r468(f, kHz="1kHz")` Takes a frequency value and returns a weighted dB value. For weightening, the ITU-R-468 standard is followed.

The math for this is taken from Wikipedia (as of 2019-08-08):

- https://en.wikipedia.org/wiki/ITU-R_468_noise_weighting

Shortened link to the archived Wikipedia page (as of 2019-08-08):

- https://bit.ly/2P29qOh

## Parameters

f: float

- The frequency value must be a value from greater 0 to 96000.

kHz: str

- Choose "1kHz" or "2kHz" filtering (default "1kHz").

## Returns

float:

- The dB weighted value of the frequency.

## Raises

ValueError:

- If parameter f is not greater 0 and smaller or equal to 96000.
- If parameter kHz is used but not "1kHz" or "2kHz".

## Examples

Some example usage can be found in `examples.py`
