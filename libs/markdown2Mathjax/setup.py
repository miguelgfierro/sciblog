#!/usr/bin/env python

import os
import sys
import distutils
from distutils.core import setup

_top_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(_top_dir, "lib"))

try:
    import markdown2Mathjax
finally:
    del sys.path[0]

setup(
    name="markdown2Mathjax",
    version=markdown2Mathjax.__version__,
    author="Matthew Young",
    author_email="matt.d.young@gmail.com",
    url="https://github.com/constantAmateur/markdown2Mathjax",
    download_url="http://pypi.python.org/pypi/markdown2Mathjax/",
    license="LICENSE.txt",
    platforms=["any"],
    py_modules=['markdown2Mathjax'],
    install_requires = ["markdown2"],
    package_dir={"": "lib"},
    description="Extend markdown2 for use with mathjax",
    long_description=open("README.txt").read(),
)
