from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath("src"))
from typing import *

from ai.greycat.greycat import GreyCat

greycat: GreyCat = GreyCat("http://localhost:8080")
gcb: list[Any | None] = greycat.call("project::get_gcb", [])
for v in gcb:
    print(v)
