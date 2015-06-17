#!/usr/bin/env python

"""ch1.py: Root Me Challenge 01 - http://challenge01.root-me.org/web-serveur/ch1/"""

import urllib2
import re


def ch1():

    f = urllib2.urlopen('http://challenge01.root-me.org/web-serveur/ch1/')

    text = f.read()
    pattern = r'password\ \:\ (.*)'
    m = re.search(pattern, text)

    return m.group(1)

def main():

    print 'Password: %s' % ch1()


if __name__ == "__main__":
    main()
