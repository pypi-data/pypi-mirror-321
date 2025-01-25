from setuptools import setup, find_packages

setup(
    name="pyritofile",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "xxhash",
        "pyzstd"
    ]
)