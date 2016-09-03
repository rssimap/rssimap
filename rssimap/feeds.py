#!/usr/bin/env python
# encoding: utf-8
"""
feeds.py

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
import os
import unittest
import feedparser
import hashlib
import time
import logging

logger = logging.getLogger("rssimap")

class Feed:
  
  def __init__(self):
    self.title = None
    self.entries = []

  def parsefeed(self, url):
    """Parse a feed"""
    
    self.feedparser_data = feedparser.parse(url)
    self.feed = self.feedparser_data['feed']
    for entry in self.feedparser_data['entries']:
        logger.debug("working on entry %s" % (repr(entry)))
        content = entry.get('content', None)
        if content is not None:
            if len(content) > 0:
                content = content[0].value
        else:
            summary_detail = entry.get('summary_detail', None)
            if summary_detail is not None:
                content = summary_detail['value']
        
        self.entries.append(FeedEntry(entry.get('title', None), entry.get('link', ''), content,
            entry.get('updated_parsed', time.gmtime()), entry.get('author', None)))
    

class FeedEntry:
    def __init__(self, title, url, text, updated, author):
      self.title = title
      self.url = url
      self.text = text
      self.updated = updated
      self.author = author
    
    def msgid(self):
      return hashlib.md5(self.url.encode('utf-8')).hexdigest()+'@pyrssimap.example.com'

class FeedTests(unittest.TestCase):
  def setUp(self):
    pass


if __name__ == '__main__':
  unittest.main()
