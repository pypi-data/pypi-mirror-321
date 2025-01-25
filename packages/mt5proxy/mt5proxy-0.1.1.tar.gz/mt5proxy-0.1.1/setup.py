#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
from setuptools import setup, find_packages

from knify import help

setup(
    name='mt5proxy',
    version='0.1.1',
    keywords='mt5proxy',
    description='Development tools for python',
    license='MIT License',
    url='https://github.com/qicongsheng/%s' % help.get_name(),
    author='qicongsheng',
    author_email='qicongsheng@outlook.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[
        'MetaTrader5',
        'knify'
    ]
)
