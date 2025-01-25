from setuptools import setup, find_packages, Extension
import numpy
import os

# Get the core directory path
core_dir = os.path.join('NChess', 'core')

# Function to collect all .c files
def find_c_files(directory):
    c_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.c'):
                c_files.append(os.path.join(root, file))
    return c_files

# Define the extension module
nchess_module = Extension(
    'NChess.core.nchess',  # Full module path
    sources=find_c_files(os.path.join(core_dir, 'src')) + find_c_files(core_dir),
    include_dirs=[
        os.path.join(core_dir, 'src'),
        numpy.get_include(),
    ],
)

setup(
    name='NChess',
    version='1.0',
    packages=find_packages(),
    ext_modules=[nchess_module],
    install_requires=[
        'numpy>=1.18.0',
    ],
    author='MNMoslem',
    author_email='normoslem256@gmail.com',
    description='chess library written in c',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MNourMoslem/NChess',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
) 