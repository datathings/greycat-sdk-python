#!/bin/bash
set -ex

VERSION=$(echo ${VERSION:-"0.0.0"} | sed 's/-/+/')

rm -rf build dist src/greycat.egg-info

sed -i -e "s/version=\"0.0.0\",/version=\"${VERSION}\",/" setup.py

python -m build -w

PY_BUILT_VERSION=$(echo ${VERSION} | sed 's/-/./g')

mv "dist/GreyCat-${PY_BUILT_VERSION}-py3-none-any.whl" "dist/greycat-${VERSION}-py3-none-any.whl"
