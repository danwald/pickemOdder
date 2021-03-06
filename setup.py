#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pandas==1.2.0', 'requests==2.25.1']

setup_requirements = []

test_requirements = []

setup(
    author="danny crasto",
    author_email='danwald79@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Parse input game stats and output rank orderd picks",
    entry_points={
        'console_scripts': [
            'pickemOdder=pickemOdder.cli:main',
            'getOddsData=pickemOdder.getoddsdata:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pickemOdder',
    name='pickemOdder',
    packages=find_packages(include=['pickemOdder', 'pickemOdder.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/danwald/pickemOdder',
    version='1.0.1',
    zip_safe=False,
)
