#!/bin/bash
set -e

VERSION=${VERSION:-"0.0.0"}

rm -rf dist

sed -i "s/^    version=\"0.0.0\",$/    version=\"${VERSION}\",/" setup.py

python -m build -w