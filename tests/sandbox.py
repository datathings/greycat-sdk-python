from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.abspath('src'))
from typing import *

from ai.greycat.greycat import GreyCat
from ai.greycat.std import std

greycat: GreyCat = GreyCat("/home/agarnier/datathings/greycat/sdk/python", [std()])
reader: GreyCat.AbiReader = greycat.openAbiRead("/home/agarnier/datathings/greycat/sdk/python/fail.gcb")
writer: GreyCat.AbiWriter = greycat.openAbiWrite("/home/agarnier/datathings/greycat/sdk/python/check.gcb")

res: Any
while reader.available() > 0:
    res = reader.read()
    if res is not None:
        print(type(res))
    print(res)
    writer.write(res)