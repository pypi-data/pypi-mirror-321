
from setuptools import setup, find_packages

setup(
    name='Topsis-MedhaSharma-102217238',  
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'topsis-cli=cli:main',  
        ]
    },
)
