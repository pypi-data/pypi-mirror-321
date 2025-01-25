from setuptools import setup, find_packages

setup(
    name='Topsis-102217223',  
    version='1.0.0',  
    author='Mehak',  
    author_email='mkaur3_be22@thapar.edu',  
    description='A Python package for TOPSIS implementation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mehakkaur13/Topsis-102217223', 
    packages=find_packages(),  
    install_requires=[
        'pandas',
        'numpy',
    ],  # List dependencies
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:topsis',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)