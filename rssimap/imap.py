#!/usr/bin/env python
# encoding: utf-8
"""
imap.py

Created by Jan on 2010-10-29.
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

import imaplib
from logging import log, ERROR, DEBUG
from email.utils import format_datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import charset

charset.add_charset('utf-8', charset.SHORTEST, charset.QP)


class Imap:
    def __init__(self, server, user, password):
        self.server = imaplib.IMAP4_SSL(server)
        self.server.login(user, password)
        self.folder_cache = {}

    def store_feedentry(self, entry, sender='PyRSSIMAP@pyrssimap.example.com', folder='INBOX'):
        # IMAP-quote folder
        imap_folder = f'"{folder}"'
        # check folder
        log(DEBUG, 'using folder "%s"', imap_folder)
        if imap_folder not in self.folder_cache:
            res, folders = self.server.list(imap_folder)
            if folders[0] is None:
                log(DEBUG, 'creating folder')
                ok, _ = self.server.create(imap_folder)
                if ok != 'OK':
                    raise ValueError('invalid folder?')
            self.folder_cache[imap_folder] = True
        # calc msg-id
        msgid = entry.msgid()
        if not self.check_msgid(msgid, imap_folder):
            log(DEBUG, 'message not yet present, appending')
            self.server.append(imap_folder, None, entry.updated, self.entry_as_mail(entry, sender))

    @staticmethod
    def entry_as_mail(entry, sender):
        entry_as_mail = MIMEMultipart('alternative')
        entry_as_mail['Subject'] = entry.title
        if entry.author is None:
            entry_as_mail['From'] = "%s <noreply@pyrssimap.example.com>" % sender
        else:
            entry_as_mail['From'] = "%s (%s) <noreply@pyrssimap.example.com>" % (sender, entry.author)
        entry_as_mail['To'] = '<nachrichten@pyrssimap.example.com>'
        entry_as_mail['Message-ID'] = "<%s>" % entry.msgid()
        if entry.updated is not None:
            entry_as_mail['Date'] = format_datetime(entry.updated)
        # entry_as_mail.set_payload("%s\n\n%s" % (entry.text, entry.url))
        entry_as_mail.set_charset(charset.Charset('UTF-8'))
        email_txt = MIMEText(f'{entry.url}\n\n{entry.text}\n\n{entry.url}', 'plain', 'utf-8')
        entry_as_mail.attach(email_txt)
        email_html = MIMEText(
            f'<html><body><a href="{entry.url}">Open</a><hr/>{entry.text}<hr/><a href="{entry.url}">Open</a></body></html>', 'html', 'utf-8')
        entry_as_mail.attach(email_html)
        return entry_as_mail.as_bytes()

    def check_msgid(self, msgid, folder):
        res, msgs = self.server.select(folder)
        if res == 'NO':
            log(ERROR, "Folderfehler %s, %s, %s" % (folder, res, msgs))
            raise NameError("Folderfehler %s, %s, %s" % (folder, res, msgs))
        res, msgs = self.server.search(None, "(HEADER Message-ID \"<%s>\")" % msgid)
        if res == 'OK' and len(msgs) > 0 and len(msgs[0]) > 0:
            return True
        else:
            return False
