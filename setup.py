#!/opt/anaconda/bin/python

# Copyright 2017 Babak Afshin-Pour
#-----------------------------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should receive a copy of the GNU General Public License
# along with this program.  See also <http://www.gnu.org/licenses/>.
#----------------------------------------------------------------------------------------- 
# Contact:
#
# babak.afshinpour@gmail.com
#-----------------------------------------------------------------------------------------



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