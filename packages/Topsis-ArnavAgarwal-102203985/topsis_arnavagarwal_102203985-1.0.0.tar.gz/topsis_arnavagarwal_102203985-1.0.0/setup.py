
from setuptools import setup, find_packages

setup(
    name='Topsis-ArnavAgarwal-102203985',  # Replace with your name and roll number
    version='1.0.0',
    author='Arnav Agarwal',
    author_email='arnavagarwal123654@gmail.com',
    description='A Python package for performing TOPSIS analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Teddyy27/Topsis-ArnavAgarwal-102203985',  # Replace with your GitHub link
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'openpyxl'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
