#!/bin/bash
set -e

VERSION_MAJOR_MINOR=`cat VERSION`
VERSION=${VERSION:-"0.0.0"}

echo "${VERSION_MAJOR_MINOR} / ${VERSION}"

sha256_hash=$(echo -n "$GET_GC_CI_PASS" | openssl dgst -sha256 | cut -d ' ' -f2)
base64url_token=$(echo -n "ci:$sha256_hash" | base64 -w 0 )
token=$(curl -s -d "[\"${base64url_token}\", false]" -X POST https://get.greycat.io/runtime::User::login | tr -d '"')

cd dist

file="greycat-${VERSION}-py2.py3-none-any.whl"

curl -s -X PUT -H "Authorization: $token" -T $file "https://get.greycat.io/files/sdk/python/${CI_COMMIT_REF_NAME}/${VERSION_MAJOR_MINOR}/${file}"
curl -s -X PUT -H "Authorization: $token" -T $file "https://get.greycat.io/files/sdk/python/${CI_COMMIT_REF_NAME}/greycat-latest-py2.py3-none-any.whl"
curl -s -X PUT -H "Authorization: $token" -d "${VERSION_MAJOR_MINOR}/${VERSION}" -H "Content-Type: text/plain" "https://get.greycat.io/files/sdk/python/${CI_COMMIT_REF_NAME}/latest"
