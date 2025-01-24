#!/usr/bin/env python
from setuptools import setup


with open("README.rst") as fh:
    long_description = fh.read()

setup(
    name="sympasoap",
    version="1.1.3",
    description="A simple Python Sympa API",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Emmy D'Anello",
    author_email="emmy.danello@animath.fr",
    url="https://gitlab.com/animath/si/py-sympa-soap",
    python_requires=">=3.6",
    install_requires=[
        "zeep>=3.0,<5.0",
    ],
    tests_require=[],
    extras_require={},
    entry_points={},
    package_dir={},
    packages=["sympasoap"],
    include_package_data=True,
    license="GPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    zip_safe=False,
)
