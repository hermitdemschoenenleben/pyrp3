import os
from distutils.command.build import build
from distutils.command.install import install
from distutils.core import setup, Extension
from pathlib import Path

from PyRedPitaya import __version__

this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    name="PyRedPitaya",
    version=__version__,
    description="Python utilities for redpitaya",
    author="Pierre Cladé",
    author_email="pierre.clade@upmc.fr",
    maintainer="Bastian Leykauf",
    maintainer_email="leykauf@physik.hu-berlin,de",
    long_description=long_description,
    long_description_content_type="text/rst",
    packages=["PyRedPitaya", "PyRedPitaya.enum"],
    install_requires=["myhdl", "rpyc", "cached_property", "numpy"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["redpitaya", "FPGA", "zynq"],
    ext_modules=[Extension('monitor',['monitor/monitor.c'])]
)
