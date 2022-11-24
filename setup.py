# copyright ############################### #
# This file is part of the Xtrack Package.  #
# Copyright (c) CERN, 2021.                 #
# ######################################### #

from pathlib import Path

from setuptools import Extension, find_packages, setup

#######################################
# Prepare list of compiled extensions #
#######################################

extensions = []

#########
# Setup #
#########

version_file = Path(__file__).parent / "boa/_version.py"
package_info = {}
with open(version_file.absolute(), "r") as fp:
    exec(fp.read(), package_info)
__version__ = package_info["__version__"]


if __name__ == "__main__":
    setup(
        name="boa",
        version=__version__,
        description="Integrated suite for beam optics and analysis",
        long_description="Integrated suite for particle accelerator beam optics and analysis",
        author="R. De Maria, F. Soubelet et al.",
        packages=find_packages(),
        ext_modules=extensions,
        install_requires=["numpy>=1.0", "cpymadtools>=1.0.0"],
        url="https://github.com/beamopticsanalysis/boa",
        license="Apache 2.0",
        download_url="https://pypi.python.org/pypi/boa",
        project_urls={
            "Bug Tracker": "https://github.com/beamopticsanalysis/boa/issues",
            "Documentation": "https://github.com/beamopticsanalysis/boa/",
            "Source Code": "https://github.com/beamopticsanalysis/boa/",
        },
    )
