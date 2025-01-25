from setuptools import setup, find_packages

setup(
    name='102206172_DHRUV',  # The name of your package on PyPI
    version='1.0.0',  # Initial version
    description='A Python implementation of the TOPSIS method for multi-criteria decision making',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Dhruv',
    author_email='dsanmotra_be22@thapar.edu.com',
    url='https://github.com/Dhruvrstar/TOPSIS',  # Your repository URL
    packages=find_packages(),
    install_requires=[
        'pandas'
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.__main__:main',  # Command-line tool entry point
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)