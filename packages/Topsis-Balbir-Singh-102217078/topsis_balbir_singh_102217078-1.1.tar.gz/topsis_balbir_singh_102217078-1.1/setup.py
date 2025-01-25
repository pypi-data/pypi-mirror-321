from setuptools import setup, find_packages

setup(
    name='Topsis-Balbir-Singh-102217078',
    version='1.1',  # Incremented from previous version
    author='Balbir Bhatia',
    author_email='balbirs2204@gmail.com',
    description='A Python package for multi-criteria decision making using the TOPSIS method.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/yourusername/your-repo',  # Update this if you have a specific project URL
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
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=['topsis', 'decision analysis', 'MCDM', 'multi-criteria decision making', 'Python']  # Added keywords
)
