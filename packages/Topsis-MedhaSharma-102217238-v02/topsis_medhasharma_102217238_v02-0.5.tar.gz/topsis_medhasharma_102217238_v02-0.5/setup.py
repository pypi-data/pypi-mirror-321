from setuptools import setup, find_packages
from pathlib import Path

# Read the content of your README file
long_description = (Path(__file__).parent / 'README.md').read_text()

setup(
    name='Topsis-MedhaSharma-102217238-v02',  
    version='0.5',
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
    long_description=long_description,  
    long_description_content_type='text/markdown', 
)
