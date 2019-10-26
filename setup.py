#!/usr/bin/env python

import setuptools
from xboringbot import version

current_version = version.version()

setuptools.setup(

    name='xboringbot',

    version=current_version,

    license='GPL-3.0',

    author='Riko',
    author_email='nobody@gmail.com',

    install_requires=[
        'python-telegram-bot',
        'Pyyaml',
    ],

    packages=[
        'xboringbot',
    ],

    entry_points={
        'console_scripts': [
            'xboringbot = xboringbot.__main__:main',
        ],
    },
    package_data={'': ['./xboringbot/material/name_chinese.txt']},

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        'Not on PyPI'
    ],

)
