#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re
import glob
try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup

dir_path = os.path.dirname(os.path.realpath(__file__))

init_string = open(os.path.join(dir_path, 'src','__init__.py')).read()

try:
    import pypandoc
    with open('README.md', 'r') as f:
        txt = f.read()
    txt = re.sub('<[^<]+>', '', txt)
    long_description = pypandoc.convert(txt, 'rst', 'md')
except ImportError:
    long_description = open('README.md').read()

setup(
    name                = 'baygaud',
    version             = '1.0.0',
    description         = 'profile decomposition tool',
    author              = 'Se-Heon Oh',
    author_email        = 'seheon.oh@sejong.ac.kr',
    url                 = 'https://github.com/seheon-oh/baygaud-PI',
    packages            = ["src"],
    keywords            = ['HI spectral line decomposition', 'nested sampling'],
    python_requires     = '>=3',
    install_requires     = [
        "aiosignal==1.3.1",
        "astropy==5.2.1",
        "attrs==22.2.0",
        "casa-formats-io==0.2.1",
        "certifi==2022.12.7",
        "charset-normalizer==3.0.1",
        "click==8.1.3",
        "cloudpickle==2.2.1",
        "contourpy==1.0.7",
        "cycler==0.11.0",
        "dask==2023.1.0",
        "distlib==0.3.6",
        "dynesty==2.0.3",
        "filelock==3.9.0",
        "fonttools==4.38.0",
        "frozenlist==1.3.3",
        "fsspec==2023.1.0",
        "grpcio==1.51.1",
        "idna==3.4",
        "joblib==1.2.0",
        "jsonschema==4.17.3",
        "kiwisolver==1.4.4",
        "llvmlite==0.39.1",
        "locket==1.0.0",
        "matplotlib==3.6.3",
        "msgpack==1.0.4",
        "numba==0.56.4",
        "numpy==1.23.5",
        "packaging==23.0",
        "partd==1.3.0",
        "Pillow==9.4.0",
        "platformdirs==2.6.2",
        "protobuf==4.21.12",
        "psutil==5.9.4",
        "pyerfa==2.0.0.1",
        "pyparsing==3.0.9",
        "pyrsistent==0.19.3",
        "python-dateutil==2.8.2",
        "PyYAML==6.0",
        "radio-beam==0.3.4",
        "ray==2.2.0",
        "requests==2.28.2",
        "scipy==1.10.0",
        "six==1.16.0",
        "spectral-cube==0.6.0",
        "tk==0.1.0",
        "toolz==0.12.0",
        "urllib3==1.26.14",
        "virtualenv==20.17.1"
        ],
    package_data        = {"": ["README.md"]},
    include_package_data=True,
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'baygaud=src.baygaud:main',
            'baygaud_classify=src.baygaud_classify:main',
        ],
    },
)
