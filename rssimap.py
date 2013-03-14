#!/usr/bin/env python
# encoding: utf-8
"""
rssimap.py

Created by Jan on 2010-08-20.
Copyright 2010 Jan <jan.rssimap.dev@gmail.com>

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

import sys
import getopt
from feeds import Feed
from imap import Imap


help_message = '''
The help message goes here.
'''


class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg


def main(argv=None):
  if argv is None:
    argv = sys.argv
  try:
    try:
      opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
    except getopt.error, msg:
      raise Usage(msg)
  
    # option processing
    for option, value in opts:
      if option == "-v":
        verbose = True
      if option in ("-h", "--help"):
        raise Usage(help_message)
      if option in ("-o", "--output"):
        output = value
  
  except Usage, err:
    print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
    print >> sys.stderr, "\t for help use --help"
    return 2

  from feed_list import feeds

  server = Imap('IMAP_SERVER_HERE', 'LOGIN_HERE', 'PASSWORD_HERE')

  for feed_name, feed_url in feeds.items():
      feed = Feed()
      feed.parsefeed(feed_url)
  
      for entry in feed.entries:
          server.store_feedentry(entry, feed_name, feed_name)


if __name__ == "__main__":
  sys.exit(main())
