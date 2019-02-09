from io import open
from os import path

from setuptools import find_packages, setup

with open(
    path.join(path.abspath(path.dirname(__file__)), "README.org"), encoding="utf-8"
) as f:
    long_description = f.read()

setup(
    name="Twister",
    version="0.1.0",
    description="Dynamic website mpv wrapper",
    entry_points={"console_scripts": ["twister=Twister.command_line:main"]},
    install_requires=["selenium"],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    url="https://github.com/amatrelan/twister",
    author="Jarmo Riikonen",
    author_email="amatrelan@gmail.com",
    classifiers=[
        "Development status :: 3",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.5",
)
