import os
import sys
sys.path.insert(0, os.path.abspath('src'))

from ai.greycat.greycat import GreyCat

greycat: GreyCat = GreyCat('http://localhost:8080')