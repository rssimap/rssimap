#!/usr/bin/env python3
# encoding: utf-8
"""
rssimap.py

Created by Jan on 2010-08-20.
Copyright 2020 Jan <jan.rssimap.dev@gmail.com>

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

import argparse
import logging
import getpass

from rssimap.feeds import Feed
from rssimap.imap import Imap
from rssimap.feed_list import feeds


def run():
    parser = argparse.ArgumentParser(description='Read RSS feeds on any device with an IMAP client.')
    parser.add_argument('-v', '--verbose', action='store_true', help='print verbose output')
    parser.add_argument('-p', '--password', default=None, help='IMAP password')
    parser.add_argument('server', default=None, help='IMAP server')
    parser.add_argument('user', default=None, help='IMAP username')
    options = parser.parse_args()

    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    if options.password is None:
        options.password = getpass.getpass('Password for %s: ' % options.user)

    logger.debug('Connecting to %s as %s', options.server, options.user)
    server = Imap(options.server, options.user, options.password)

    for feed_name, feed_url in feeds.items():
        feed = Feed()
        logger.debug("parsing feed %s" % feed_url)
        feed.parsefeed(feed_url)

        logger.debug("sending feed entries to server")
        for entry in feed.entries:
            logger.debug("storing entry %s", entry.title)
            server.store_feedentry(entry, feed_name, feed_name)
