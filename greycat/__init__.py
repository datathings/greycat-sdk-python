from .greycat import *
from .std import *

try:
    from .algebra import *
except ModuleNotFoundError:
    pass

try:
    from .decisiontrees import *
except ModuleNotFoundError:
    pass

try:
    from .patterns import *
except ModuleNotFoundError:
    pass

try:
    from .sql import *
except ModuleNotFoundError:
    pass

try:
    from .useragent import *
except ModuleNotFoundError:
    pass