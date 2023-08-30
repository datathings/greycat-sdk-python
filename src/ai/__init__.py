import os
import sys

# Get the path to the directory containing this module (__init__.py)
module_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory of the module directory to sys.path
parent_dir = os.path.dirname(module_dir)
sys.path.insert(0, parent_dir)

# Add the module directory to the __path__ attribute of the package
__path__.append(module_dir)

# Import submodules so that they are available when the package is imported
from .greycat import algebra_n, greycat, std_n, std