#!/bin/bash
set -ex

VERSION=${VERSION:-"0.0.0"}

rm -rf dist

sed -i -e "s/version=\"0.0.0\",/version=\"${VERSION}\",/" setup.py
sed -i -e "s/version = \"0.0.0\"/version = \"${VERSION}\"/" pyproject.toml

python -m pip install --upgrade pip
python -m pip install build
python -m build -w
