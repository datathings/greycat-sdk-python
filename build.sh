#!/bin/bash

echo "DEBUG: 0"

set -ex

echo "DEBUG: 1"

VERSION=${VERSION:-"0.0.0"}

echo "DEBUG: 2"

rm -rf dist

echo "DEBUG: 3"

sed -i -e "s/^    version=\"0.0.0\",$/    version=\"${VERSION}\",/" setup.py

echo "DEBUG: 4"

python -m build -w

echo "DEBUG: 5"