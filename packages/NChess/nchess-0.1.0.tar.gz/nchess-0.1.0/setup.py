from setuptools import setup, find_packages

setup(
    name='nchess',
    version='0.1.0',
    packages=find_packages(),
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