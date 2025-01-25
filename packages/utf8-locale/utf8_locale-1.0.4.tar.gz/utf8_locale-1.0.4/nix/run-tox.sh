#!/bin/sh
#
# SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
# SPDX-License-Identifier: BSD-2-Clause

set -e

: "${PY_MINVER_MIN:=10}"
: "${PY_MINVER_MAX:=13}"

for pyver in $(seq -- "$PY_MINVER_MIN" "$PY_MINVER_MAX"); do
	tests/cleanpy.sh
	printf -- '\n===== Running tests for Python 3.%s\n\n\n' "$pyver"
	nix-shell --pure --argstr py-ver "$pyver" nix/python-tox.nix
	printf -- '\n===== Done with Python 3.%s\n\n' "$pyver"
done
