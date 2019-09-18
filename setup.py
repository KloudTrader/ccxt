# prefer setuptools over distutils
from setuptools import setup, find_packages

# use a consistent encoding
from codecs import open
from os import path
import json
import sys

is_python_2 = sys.version_info < (3, 0)

here = path.abspath(path.dirname(__file__))
root = path.dirname(here)

readme = path.join(here, 'README.rst')
#package_json = path.join(here, 'package.json')

# a workaround when installing locally from git repository with pip install -e .
'''
if not path.isfile(package_json):
    package_json = path.join(root, 'package.json')
'''
# long description from README file
with open(readme, encoding='utf-8') as f:
    long_description = f.read()

# version number and all other params from package.json
'''
with open(package_json, encoding='utf-8') as f:
    package = json.load(f)
'''
setup(

    name='ccxt',
    version='0.0.1',

    description="KloudTrader's extended version of ccxt's python module. Powers Libkloudtrader's crypto trading.",
    long_description="KloudTrader's extended version of ccxt's python module. Powers Libkloudtrader's crypto trading.",

    # will switch from rst to md shortly
    # long_description_content_type='text/markdown',

    url="",

    author='KloudTrader',
    author_email='admin@kloudtrader.com',

    license="",

    classifiers=[
        "KloudTrader",
        "ccxt"
    ],

    keywords="",
    packages=find_packages(exclude=['ccxt.async_support*'] if is_python_2 else []),

    install_requires=[
        'setuptools>=38.5.1',
        'certifi>=2018.1.18',
        'requests>=2.18.4',
        'cryptography>=2.6.1',
        'web3'
    ],

    extras_require={
        ':python_version>="3.5.2"': [
            'aiohttp>=3.0.1',
            'aiodns==1.1.1',
            'yarl==1.1.0',
        ],
        'qa': [
            'flake8==3.5.0'
        ],
        'doc': [
            'Sphinx==1.7.0'
        ]
    }
)
