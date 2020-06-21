#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup

def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()

setup(
    name='jinja2-strcase',
    version='0.0.1',
    author='Marek Chmiel',
    maintainer='Marek Chmiel',
    license='MIT',
    url='https://github.com/marchmiel/jinja2-strcase',
    description='A python package for converting string case in jinja2 templates',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    packages=[
        'jinja2_strcase',
    ],
    package_dir={'jinja2_strcase': 'jinja2_strcase'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'jinja2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
    ],
    keywords=['jinja2', 'extension', 'strcase'],
)