from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()

setup(
    name='102203525_TOPSIS',
    version='0.1.2',
    packages=find_packages(),
    description='A Python package for TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)',
    long_description= long_desc,
    long_description_content_type='text/markdown',
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