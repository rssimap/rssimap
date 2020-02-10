rssimap
=======

Read RSS feeds on any device with an IMAP client.

## Installation

### rssimap
* Clone/download https://github.com/rssimap/rssimap

### Dependencies
* Python 3.7
    * it most likely works with older versions as well
    * you should have it installed already or know how if you do not
* feedparser module
    * `pip install feedparser` or
    * FreeBSD: `pkg install py37-feedparser`
    * Debian/Ubuntu: `apt install python3-feedparser`
    * macOS: `port install py37-feedparser`
* dateutil module
    * `pip install python-dateutil`
    * FreeBSD: `pkg install py37-dateutil`
    * Debian/Ubuntu: `apt install python3-dateutil`
    * macOS: `port install py37-dateutil`
* Install dependencies
    * Either as above system-wide
    * Or into a virtual environment:
        * `python3 -m venv rssimap_venv`
        * `. rssimap_venv/bin/activate`
        * `(rssimap_venv) $ python setup.py develop`

## Configuration

* Add your feeds to feed_list.py or convert .opml with convert.py

## Running

If you created a virtual environment above, just run
* `(rssimap_venv) $ rssimap <user> <imap-server.example.com>`
* or `python3 -m rssimap <user> <imap-server.example.com>` otherwise

If everything looks ok and you like rssimap, add it to your crontab - 
the IMAP server password can be set via `-p <password>`.
Please refrain from using your real IMAP account at the moment, get another one exclusively for this.
You can run rssimap from some dedicated server or on your client, but should try to avoid running multiple instances at the same time (never done this, but probably even then nothing too bad happens).

## Bugs

I have been running this for close to ten years and it seems to work quite ok how it is.
Apart from that:

* The way it interacts with the IMAP server when storing new messages is not the 'right' way and somewhat dumb
* Installation, configurability and error reporting is obviously not that good at the moment

If anyone cares, I will work on all of this and make this a package at PyPI.  Please submit bugs and patches! 
