from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='topsis-102203958',
    version='1.0.8',
    description='A Python package to calculate TOPSIS scores',
    long_description=long_description,  # Include the long description
    long_description_content_type='text/markdown',  # Specify Markdown as the content type
    author='Pratyush Sharma',
    author_email='pratyushksk@gmail.com',
    packages=find_packages(),
    py_modules=['pratyush_102203958'],  # Use the new module name
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis=pratyush_102203958:main',  # Update to use the new module and main function
        ],
    },
)
