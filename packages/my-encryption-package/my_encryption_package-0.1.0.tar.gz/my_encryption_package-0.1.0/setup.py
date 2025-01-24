# setup.py

from setuptools import setup, find_packages

setup(
    name='my_encryption_package',
    version='0.1.0',
    description='A package for various encryption techniques',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your_email@example.com',
    packages=find_packages(),
    install_requires=[
        'pycryptodome',  # For AES encryption
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
