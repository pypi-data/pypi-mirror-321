from setuptools import setup, find_packages, Extension
import numpy
import os
import sys
from setuptools.command.build_ext import build_ext

# Get the core directory path
core_dir = os.path.join('NChess', 'core')

class CustomBuildExtCommand(build_ext):
    def build_extensions(self):
        # Customize compiler settings if needed
        if sys.platform.startswith('linux'):
            # Add specific flags for Linux
            for ext in self.extensions:
                ext.extra_compile_args = ['-fPIC']
        try:
            build_ext.build_extensions(self)
        except Exception as e:
            print(f"Warning: Failed to build extension: {e}")
            # Continue installation without the extension

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
    version='1.0.1',
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
    cmdclass={
        'build_ext': CustomBuildExtCommand,
    },
    python_requires='>=3.7',
) 