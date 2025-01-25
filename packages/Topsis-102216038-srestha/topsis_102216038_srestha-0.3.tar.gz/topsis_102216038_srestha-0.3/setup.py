from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "Readme.md").read_text()  # Gets the long description from the Readme file

from setuptools import setup, find_packages

setup(
    name="Topsis-102216038-srestha",
    version="0.3",
    packages=find_packages(),
    install_requires=["numpy", "pandas"],
    description="A package to perform TOPSIS analysis",
    author="Srestha jain",
    url="https://github.com/SresthaJain/TOPSIS-PACKAGE-",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
