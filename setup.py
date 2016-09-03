"""
Copyright 2016 Jan <jan.rssimap.dev@gmail.com>

This file is part of rssimap.

rssimap is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

rssimap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with rssimap.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='rssimap',
    version='0.5.0',
    license='GPLv3',
    url = 'https://github.com/rssimap/rssimap',
    download_url = 'https://github.com/rssimap/rssimap/zipball/master',
    author = 'Jan',
    author_email = 'jan.rssimap.dev@gmail.com',
    description = 'Read RSS feeds on any device with an IMAP client.',
    long_description = open(os.path.join(here, 'README.md')).read(),
    classifiers = ['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Intended Audience :: End Users/Desktop',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
                   'Topic :: Communications :: Email',
                   'Topic :: Internet',
                   'Topic :: Utilities',
                   'Environment :: Console',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   # TODO python 3
                  ],
    packages=find_packages(),
    install_requires = ['feedparser'],
    entry_points={'console_scripts': ['rssimap = rssimap.__main__:run']},
    )
