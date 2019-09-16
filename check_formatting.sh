#!/usr/bin/env sh

set -e

. ./format_code.sh

exec git diff --exit-code
