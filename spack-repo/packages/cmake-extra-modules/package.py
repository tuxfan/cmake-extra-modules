# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class CMakeExtraModules(CMakePackage):
    '''CMake modules for projects that have not yet adopted modern CMake.'''
    homepage = 'http://github.com:cmake-extra-modules.git'
    git      = 'http://github.com:cmake-extra-modules/cmake-extra-modules.git'
