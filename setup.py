"""setup.py"""
from setuptools import setup
from codecs import open as codecs_open

with codecs_open('README.md', 'r', 'utf-8') as f:
    README = f.read()

setup(
     # Application name:
    name='FortigateApi',

    # Version number:
    version='1.11',
    
    # Description:
    description='Access Fortigate REST API in python',
    long_description=open("README.rst").read(),
    
    # Application author details:
    author='Original author David Chayla and Pypi maintainer AdmiralSpark',
    author_email='null',
    
    # Details:
    url='https://github.com/admiralspark/FortigateApi',
    download_url='https://github.com/admiralspark/FortigateApi/archive/1.11.tar.gz', 

    # License
    license='GPL-3.0',
    
    # Packages:
    packages=['FortigateApi'],
    
    # Searchables:
    keywords=['fortigate', 'REST', 'network'],
)
