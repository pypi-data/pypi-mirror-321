from setuptools import setup, find_packages, Extension
import numpy
import os
import sys
from setuptools.command.build_ext import build_ext


setup(
    name='NChess',
    version='1.0.5',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'NChess.core': ['*.pyd', '*.so'],
    },
    install_requires=['numpy>=1.18.0'],
    author='MNMoslem',
    author_email='normoslem256@gmail.com',
    description='chess library written in c',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MNourMoslem/NChess',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
) 