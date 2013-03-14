rssimap
=======

Read RSS feeds on any device with an IMAP client.

## Installation

### Dependencies
* Python 2.7 
    * it most likely works with older versions as well
    * you should have it installed already or know how if you do not
* feedparser module
    * pip install feedparser or
    * FreeBSD: portmaster textproc/py-feedparser
    * Debian/Ubuntu: apt-get install python-feedparser
    * Mac OS: port install py27-feedparser

### rssimap
* You already have it or should just clone/download this thing here

## Configuration

* Add your feeds to feed_list.py or convert .opml with convert.py
* Add IMAP server, login and password to rssimap.py, adjust the line `server = Imap('IMAP_SERVER_HERE', 'LOGIN_HERE', 'PASSWORD_HERE')`
* Please **do not use your real IMAP account** at the moment, get another one exclusively for this 

## Running

Just run rssimap.py. If everything looks ok and you like it, add it to your crontab.
You can run it from some dedicated server or on your client, but should try to avoid running multiple instances at the same time (never done this, but probably even then nothing too bad happens).

## Bugs

I have been running this for close to two years and it seems to work quite ok how it is.
Apart from that:

* The way it interacts with the IMAP server when storing new messages is not the 'right' way and somewhat dumb
* Installation, configurability and error reporting is obviously not that good at the moment

If anyone cares, I will work on all of this and make this a package at PyPI.  Please submit bugs and patches! 
