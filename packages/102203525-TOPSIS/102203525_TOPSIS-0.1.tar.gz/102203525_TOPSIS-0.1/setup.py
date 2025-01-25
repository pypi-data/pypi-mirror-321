from setuptools import setup, find_packages

setup(
    name='102203525_TOPSIS',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'run-topsis = 102203525_TOPSIS.102203525:main',
        ],
    },
)