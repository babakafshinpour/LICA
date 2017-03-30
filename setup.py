#!/opt/anaconda/bin/python

# System imports
from distutils.core import *
from distutils      import sysconfig

# Third-party modules - we depend on numpy for everything
import numpy

# Obtain the numpy include directory.  This logic works across numpy versions.
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

# mi extension module
_mi = Extension("_mi",
                   ["mi_wrap.c","mi.c"],
                   include_dirs = [numpy_include],
                    extra_compile_args = ["-std=gnu99"]
                   )

# ezrange setup
setup(  name        = "mi",
        description = "mutual ifnromation package for estimating ICA, and dependencies between variables",
        author      = "Babak Afshin-Pour",
        author_email= "babak@rtdsinc.com",
        version     = "1.1",
        ext_modules = [_mi],
        headers=["./mi.h"]
        )