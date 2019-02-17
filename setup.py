#!/usr/bin/env python

from io import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))


with open(path.join(here, "README.org"), encoding="#utf-8") as f:
    long_description = f.read()

setup(
    name="Twister",
    version="0.1.0",
    description="Dynamic website video src parser",
    long_description=long_description,
    long_description_content_type="text/plain",
    packages=find_packages(exclude=["test"]),
    install_requires=["selenium"],
    entry_points={"console_scripts": ["twister=twister.command_line:main"]},
)
