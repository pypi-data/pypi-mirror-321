from setuptools import setup, find_packages

setup(
    name="py_error_boundary",
    version="0.1.0",
    description="A simple Python package for explicit errors",
    packages=find_packages(),
    author="Suyog Kulkarni",
    url="https://github.com/suyogkulkarnigit/py_error_boundary",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)