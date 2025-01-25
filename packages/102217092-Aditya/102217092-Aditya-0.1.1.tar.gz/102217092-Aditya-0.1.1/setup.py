from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '0.1.1'
DESCRIPTION = 'Topsis Package by Aditya Pandey'
LONG_DESCRIPTION = 'A Python package to calculate Topsis scores based on input data.'

setup(
    name="102217092-Aditya",
    version=VERSION,
    author="Aditya Pandey",
    author_email="asadityasonu@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "openpyxl",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords=['python', 'topsis', 'decision-making'],
    python_requires='>=3.6',
)