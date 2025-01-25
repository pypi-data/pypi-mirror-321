from setuptools import setup, find_packages

setup(
    name='topsis-102203958',
    version='1.0.0',
    description='A Python package to calculate TOPSIS scores',
    author='Pratyush Sharma',
    author_email='pratyushksk@gmail.com',
    packages=find_packages(),
    py_modules=['102203958'],
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis=102203958:main',
        ],
    },
)
