"""Setup.py for the Binder project."""
import os
import unittest
from os.path import dirname
from typing import Dict, List

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

my_dir = dirname(__file__)


def binder_test_suite() -> unittest.TestSuite:
    """Test suite for Binder tests"""
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(os.path.join(my_dir, "tests"), pattern="test_*.py")
    return test_suite


dev = [
    "black",
    "flake8",
    "flake8-colors",
    "pylint",
    "isort",
    "pre-commit",
    "wheel",
]

EXTRAS_REQUIREMENTS: Dict[str, List[str]] = {
    "dev": dev,
}

setuptools.setup(
    name="binder",
    version="0.0.1",
    extras_require=EXTRAS_REQUIREMENTS,
    install_requires=[
        "flask",
    ],
    description="A scrap attachment application.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    test_suite="setup.binder_test_suite",
)
