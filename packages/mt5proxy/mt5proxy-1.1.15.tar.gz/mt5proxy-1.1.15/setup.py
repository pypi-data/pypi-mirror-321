#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
from setuptools import setup, find_packages

from mt5proxy import help

setup(
    name=help.get_name(),
    version=help.get_version(),
    keywords=help.get_name(),
    description='Mt5 http proxy for python.',
    license='MIT License',
    url='https://github.com/qicongsheng/%s' % help.get_name(),
    author='qicongsheng',
    author_email='qicongsheng@outlook.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='Windows',
    install_requires=[
        'MetaTrader5',
        'flask',
        'pandas',
        'pytz'
    ],
    entry_points={
        'console_scripts': [
            'mt5proxy = mt5proxy.__main__:main'
        ]
    }
)
