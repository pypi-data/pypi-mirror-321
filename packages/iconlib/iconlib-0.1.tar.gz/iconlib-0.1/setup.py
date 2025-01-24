from setuptools import setup, find_packages
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='Iconlib',
    version='0.1',
    packages=find_packages(),
    author='Vikhram S',
    author_email='Vikhrams@saveetha.ac.in',
    description='A Python library for exploring the Constitution of India.',

    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache 2.0',
     project_urls={
           'Source Repository': 'https://github.com/Vikhram-S/Iconlib' #replace with your github source
    }
)
