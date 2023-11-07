from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath("src"))
from typing import *

from greycat import *

greycat: GreyCat = GreyCat("http://localhost:8080", username="admin", password="admin")
gcb: list[Any | None] = greycat.call("project::get_gcb", [])
for v in gcb:
    print(greycat.call("project::display", [v]))
