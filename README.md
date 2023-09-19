# GreyCat Python SDK

## Prerequisites

- Python >= 3.8
- pip

## Install

In some operating systems python executable is exposed as `python3` and others `python`. Please adapt the examples below according to your system.

- Python SDK: 
  - For the impatients:
    ```bash
    python3 -m pip install https://get.greycat.io/files/sdk/python/testing/greycat-latest-py3-none-any.whl
    ```
  - For picking a specific version, necessary for requirements to not fail with every greycat update (as the latest wheel changes, its checksum with it):
    ```bash
    python3 -m pip install https://get.greycat.io/files/sdk/python/testing/6.1/greycat-6.1.32+testing-py3-none-any.whl
    ```
    As the version above is doomed to be outdated, more recent versions can be checked at https://get.greycat.io/files/sdk/python/testing/