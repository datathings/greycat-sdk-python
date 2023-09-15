#!/bin/bash
set -ex

VERSION=${VERSION:-"0.0.0"}

rm -rf build dist src/greycat.egg-info

sed -i -e "s/version=\"0.0.0\",/version=\"${VERSION}\",/" setup.py

python -m build -w

mv "dist/GreyCat-${VERSION}-py3-none-any.whl" "dist/greycat-${VERSION}-py3-none-any.whl"
