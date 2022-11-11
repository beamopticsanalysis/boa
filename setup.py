# copyright ############################### #
# This file is part of the Xtrack Package.  #
# Copyright (c) CERN, 2021.                 #
# ######################################### #

from setuptools import setup, find_packages, Extension
from pathlib import Path

#######################################
# Prepare list of compiled extensions #
#######################################

extensions = []

#########
# Setup #
#########

version_file = Path(__file__).parent / 'boa/_version.py'
dd = {}
with open(version_file.absolute(), 'r') as fp:
    exec(fp.read(), dd)
__version__ = dd['__version__']

setup(
    name='boa',
    version=__version__,
    description='Integrated suite for beam optics and analysis',
    long_description='Integrated suite for particle accelerator beam optics and analysis',
    author='R. De Maria, F. Soubelet et al.',
    packages=find_packages(),
    ext_modules = extensions,
    install_requires=[
        'numpy>=1.0',
        ],
    url='https://github.com/beamopticsanalysis/boa',
    license='Apache 2.0',
    download_url="https://pypi.python.org/pypi/boa",
    project_urls={
            "Bug Tracker": "https://github.com/beamopticsanalysis/boa/issues",
            "Documentation": 'https://github.com/beamopticsanalysis/boa/',
            "Source Code": "https://github.com/beamopticsanalysis/boa/",
        },
    )
