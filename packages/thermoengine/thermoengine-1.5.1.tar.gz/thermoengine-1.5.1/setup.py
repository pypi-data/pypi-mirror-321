#!/usr/bin/env python
""" file: setup.py
    modified: Mark S. Ghiorso, OFM Research
    date: June 12, 2017, rev June 27, 2017, rev cython Dec 19, 2019, rev Dec 31, 2022

    description: Distutils installer script for thermoengine.
"""
from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy
import os

from sys import platform
if platform == "linux" or platform == "linux2":
    from distutils import sysconfig
    libs = ['/usr/local/lib']
    includes = ['/usr/include/gsl']
elif platform == "darwin":
    libs = ['/usr/local/lib']
    includes = ['/usr/include/gsl']
elif platform == "win32":
    vcpkg_root = os.getenv('VCPKG_ROOT', 'C:\\vcpkg')  # Set your vcpkg path
    libs = [
        os.path.join(vcpkg_root, 'installed', 'x64-windows', 'lib'),
        os.path.join(vcpkg_root, 'installed', 'x64-windows', 'bin'),
    ]
    includes = [
        os.path.join(vcpkg_root, 'installed', 'x64-windows', 'include'),
        os.path.join(vcpkg_root, 'installed', 'x64-windows', 'include')
    ]

extensions = [
    Extension(
        "thermoengine.aqueous",
        sources=["thermoengine/aqueous/aqueous.pyx",
        "thermoengine/aqueous/swim.c",
        "thermoengine/aqueous/born.c",
        "thermoengine/aqueous/duanzhang.c",
        "thermoengine/aqueous/holten.c",
        "thermoengine/aqueous/wagner.c",
        "thermoengine/aqueous/zhangduan.c",
        "thermoengine/aqueous/FreeSteam2.1/b23.c",
        "thermoengine/aqueous/FreeSteam2.1/backwards.c",
        "thermoengine/aqueous/FreeSteam2.1/bounds.c",
        "thermoengine/aqueous/FreeSteam2.1/common.c",
        "thermoengine/aqueous/FreeSteam2.1/derivs.c",
        "thermoengine/aqueous/FreeSteam2.1/region1.c",
        "thermoengine/aqueous/FreeSteam2.1/region2.c",
        "thermoengine/aqueous/FreeSteam2.1/region3.c",
        "thermoengine/aqueous/FreeSteam2.1/region4.c",
        "thermoengine/aqueous/FreeSteam2.1/solver2.c",
        "thermoengine/aqueous/FreeSteam2.1/steam.c",
        "thermoengine/aqueous/FreeSteam2.1/steam_ph.c",
        "thermoengine/aqueous/FreeSteam2.1/steam_ps.c",
        "thermoengine/aqueous/FreeSteam2.1/steam_pT.c",
        "thermoengine/aqueous/FreeSteam2.1/steam_pu.c",
        "thermoengine/aqueous/FreeSteam2.1/steam_pv.c",
        "thermoengine/aqueous/FreeSteam2.1/steam_Ts.c",
        "thermoengine/aqueous/FreeSteam2.1/steam_Tx.c",
        "thermoengine/aqueous/FreeSteam2.1/surftens.c",
        "thermoengine/aqueous/FreeSteam2.1/thcond.c",
        "thermoengine/aqueous/FreeSteam2.1/viscosity.c",
        "thermoengine/aqueous/FreeSteam2.1/zeroin.c"],
        include_dirs=['./thermoengine/aqueous', './thermoengine/aqueous/FreeSteam2.1', numpy.get_include()] + includes,
        extra_compile_args=['-O3', '-DNPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION'],
        libraries=['gsl'],
        library_dirs= libs, 
        runtime_library_dirs= [] 
    ),
]

if platform == "linux" or platform == "linux2":
    sysconfig.get_config_vars()['CC'] = 'clang'
    sysconfig.get_config_vars()['CXX'] = 'clang++'
    sysconfig.get_config_vars()['CCSHARED'] = '-fPIC'
    sysconfig.get_config_vars()['LDSHARED'] = 'clang -shared'

def readme():
    with open('README.rst') as f:
        return f.read()


setup(
      packages=find_packages(where='.'),
      # packages = ['thermoengine', 'thermoengine.aqueous'],
      ext_modules = cythonize(extensions),
)
