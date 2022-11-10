from setuptools import setup, find_packages

#######################################
# Prepare list of compiled extensions #
#######################################

extensions = []


#########
# Setup #
#########

setup(
    name='boac',
    version='0.0.1',
    description='Integrated suite for beam optics and analysis',
    long_description='Integrated suite for particle accelerator beam optics and analysis',
    author='R. De Maria, F. Soubelet et al.',
    packages=find_packages(),
    ext_modules = extensions,
    install_requires=[
        'numpy>=1.0',
        ],
    url='https://github.com/beamopticsanalysis/boac',
    license='Apache 2.0',
    download_url="https://pypi.python.org/pypi/boac",
    project_urls={
            "Bug Tracker": "https://github.com/beamopticsanalysis/boac/issues",
            "Documentation": 'https://github.com/beamopticsanalysis/boac/',
            "Source Code": "https://github.com/beamopticsanalysis/boac/",
        },
    )
