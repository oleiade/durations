#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup

root = os.path.abspath(os.path.dirname(__file__))

version = __import__('durations').__version__

setup(
    name='durations',
    version=version,
    license='MIT',

    author='Oleiade',
    author_email='tcrevon@gmail.com',
    url='http://github.com/oleiade/durations',
    keywords='',

    packages=[
        'durations',
    ],
)
