from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()  # Gets the long description from the Readme file

setup(
    name='Topsis-102216038-srestha',
    version='0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Make sure to add a comma after numpy
    ],
    author='Srestha Jain',
    description='This is the short description',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    project_urls={
        'Source Repository': 'https://github.com/SresthaJain/TOPSIS/tree/main'  # Replace with your GitHub source
    }
)# setup.py
