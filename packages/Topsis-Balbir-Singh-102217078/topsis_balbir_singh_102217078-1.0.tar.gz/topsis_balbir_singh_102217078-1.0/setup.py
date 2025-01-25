from setuptools import setup, find_packages
import os

# Function to read the contents of the README file
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

setup(
    name='Topsis-Balbir-Singh-102217078',
    version='1.0',  # Remember to update this if you are making a new release
    author='Balbir Bhatia',
    author_email='balbirs2204@gmail.com',
    description='A Python package for multi-criteria decision making using the TOPSIS method.',
    long_description=read('README.md'),  # Sets the long description to the contents of README.md
    long_description_content_type='text/markdown',  # Important for rendering Markdown correctly on PyPI
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'topsis=topsis_Balbir_102217078.topsis:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',  # Update the status as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Make sure this matches your license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
