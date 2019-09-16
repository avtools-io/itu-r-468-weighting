#!/usr/bin/env bash

isort *.py itu_r_468_weighting/*.py tests/*.py
black *.py itu_r_468_weighting/*.py tests/*.py
