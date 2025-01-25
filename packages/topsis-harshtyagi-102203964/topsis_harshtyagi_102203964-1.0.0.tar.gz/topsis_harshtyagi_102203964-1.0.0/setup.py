from setuptools import setup, find_packages

setup(
    name='topsis_harshtyagi_102203964',
    version='1.0.0',
    author='Harsh Tyagi',
    author_email='htyagi_be22@thapar.edu', 
    description='A Python implementation of the TOPSIS method for multi-criteria decision making.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/harshtyagi102203964/topsis',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
