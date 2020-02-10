#!/usr/bin/env python

import setuptools
from itsctfbot import version

current_version = version.version()

setuptools.setup(

    name='itsctfbot',

    version=current_version,

    license='GPL-3.0',

    author='Riko',
    author_email='xxy1836@gmail.com',

    install_requires=[
        'python-telegram-bot',
        'Pyyaml',
    ],

    packages=[
        'itsctfbot',
    ],

    entry_points={
        'console_scripts': [
            'itsctfbot = itsctfbot.__main__:main',
        ],
    },
    # package_data={'': ['./itsctfbot/material/name_chinese.txt']},

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        'Not on PyPI'
    ],

)
