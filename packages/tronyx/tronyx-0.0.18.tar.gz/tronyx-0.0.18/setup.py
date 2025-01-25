from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() #Gets the long description from Readme file

setup(
    name='tronyx',
    version='0.0.18',
    packages=find_packages(),
    install_requires=[
         'requests',
    ],  # Add a comma here
    author='promobro',
    author_email='promobro@protonmail.com',
    description='tronyx library for Python',

    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
     project_urls={
           'Source Repository': 'https://github.com/promobro/tronyx' #replace with your github source
    }
)
