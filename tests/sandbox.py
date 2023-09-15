from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.abspath('src'))
from typing import *

from greycat import *

greycat: GreyCat = GreyCat("/home/agarnier/datathings/greycat/sdk/python")
reader: GreyCat.AbiReader = greycat.openAbiRead("/home/agarnier/datathings/greycat/sdk/python/out.gcb")
writer: GreyCat.AbiWriter = greycat.openAbiWrite("/home/agarnier/datathings/greycat/sdk/python/check.gcb")

res: Any
while reader.available() > 0:
    res = reader.read()
    if res is not None:
        print(type(res))
    print(res)
    writer.write(res)