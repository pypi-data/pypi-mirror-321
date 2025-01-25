from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() #Gets the long description from Readme file

setup(
    name='102203816-Topsis',
    version='0.0',
    packages=find_packages(),
    install_requires=[
        'pandas','numpy','sys',
    ],  # Add a comma here
    author='Ayushi Rathore',
    description='This package performs topsis on your data',

    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
     project_urls={
           'Source Repository': 'https://github.com/ayu-shiirathore/Topsis_Package' 
    }
)
