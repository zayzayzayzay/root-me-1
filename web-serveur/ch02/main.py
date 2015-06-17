#!/usr/bin/env python

"""ch1.py: Root Me Challenge 02 - http://challenge01.root-me.org/web-serveur/ch1/"""

import urllib2
import re

BASE_URL = "http://challenge01.root-me.org/web-serveur/ch2/"

def ch02():

    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Admin')]
    response = opener.open(BASE_URL)

    pattern = r'Password\ \:\ (.*)'
    m = re.search(pattern, response.read())

    return m.group(1).split('</h3>')[0]


def main():

    print 'Password: %s' % ch02()


if __name__ == "__main__":
    main()
