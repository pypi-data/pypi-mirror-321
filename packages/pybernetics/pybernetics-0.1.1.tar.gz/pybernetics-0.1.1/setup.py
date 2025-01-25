from setuptools import setup, find_packages

"""
Setup
=====

Notes:
------
- This file is subject to unnoted changes, as it is still in the development phase.

- This is a simple setup.py file for the Python package. It is used to install the package and its dependencies using pip.
"""

setup(
    name="pybernetics",
    version="0.1.1",
    author="Marco Farruggio",
    author_email="marcofarruggiopersonal@gmail.com",
    description="Pybernetics is a lightweight toolkit for the development and training of neural networks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/WateryBird/pybernetics",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",

        # Topics
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",

        # License
        "License :: OSI Approved :: MIT License",

        # Operating System
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
    ],
    python_requires=">=3.7",
)