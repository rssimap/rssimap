#!/usr/bin/env python
# encoding: utf-8
"""
imap.py

Created by Jan on 2010-10-29.
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
import imaplib
from logging import log, ERROR, DEBUG
import email.message
from time import mktime
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import charset
charset.add_charset('utf-8', charset.SHORTEST, charset.QP)

import imap_utf7

class Imap:
  def __init__(self, server, user, password, port=None):
    self.server = imaplib.IMAP4_SSL(server)
    self.server.login(user, password)
    self.folder_cache = {}
  
  def store_feedentry(self, entry, sender = 'PyRSSIMAP@pyrssimap.example.com', folder='INBOX'):
    # check folder
    folder_utf7 = imap_utf7.encode(folder)
    if not self.folder_cache.has_key(folder):
        res, folders = self.server.list(folder_utf7)
        if folders[0] is None:
            self.server.create(folder_utf7)
        self.folder_cache[folder] = True
    # calc msg-id
    msgid = entry.msgid()
    if not self.check_msgid(msgid, folder):
        self.server.append(folder_utf7, None, entry.updated, self.entry_as_mail(entry, sender))

  def entry_as_mail(self, entry, sender):
    entry_as_mail = MIMEMultipart('alternative')
    entry_as_mail['Subject'] = entry.title
    if entry.author is None:
        entry_as_mail['From'] = "%s <noreply@pyrssimap.example.com>" % sender
    else:
        entry_as_mail['From'] = "%s (%s) <noreply@pyrssimap.example.com>" % (sender, entry.author)
    entry_as_mail['To'] = '<nachrichten@pyrssimap.example.com>'
    entry_as_mail['Message-ID'] = "<%s>" % entry.msgid()
    if entry.updated is not None:
        entry_as_mail['Date'] = formatdate(mktime(entry.updated))
    #entry_as_mail.set_payload("%s\n\n%s" % (entry.text, entry.url))
    entry_as_mail.set_charset(charset.Charset('UTF-8'))
    entry_as_mail.attach(MIMEText("%s\n\n%s\n\n%s".encode('utf-8') % (entry.url, entry.text, entry.url), 'plain', 'utf-8'))
    entry_as_mail.attach(MIMEText("<html><body><a href=\"%s\">Open</a><hr/>%s<hr/><a href=\"%s\">Open</a></body></html>".encode('utf-8') % (entry.url, entry.text, entry.url), 'html', 'utf-8'))
    return entry_as_mail.as_string()

  def check_msgid(self, msgid, folder):
    folder_utf7 = imap_utf7.encode(folder)
    res, msgs = self.server.select(folder_utf7)
    if res == 'NO':
        log(ERROR, "Folderfehler %s, %s, %s" % (folder, res, msgs))
        raise NameError("Folderfehler %s, %s, %s" % (folder, res, msgs))
    res, msgs = self.server.search(None, "(HEADER Message-ID \"<%s>\")" % msgid)
    if res == 'OK' and len(msgs) > 0 and len(msgs[0]) > 0:
        return True
    else:
        return False

class imapTests(unittest.TestCase):
  def setUp(self):
    pass


if __name__ == '__main__':
  unittest.main()
