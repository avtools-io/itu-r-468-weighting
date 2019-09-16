#!/usr/bin/env sh

set -e
set -x

. ./format_code.sh

exec git diff --exit-code
