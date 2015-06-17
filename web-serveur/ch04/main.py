#!/usr/bin/env python

"""main.py: Root Me Challenge 04 - http://challenge01.root-me.org/web-serveur/ch4/"""

import urllib2
import re

BASE_URL = "http://challenge01.root-me.org/web-serveur/ch4/"

def ch02():

    url = BASE_URL + "admin/backup/admin.txt"

    f = urllib2.urlopen(url)

    text = f.read()
    pattern = r'Password\ \/\ Mot\ de\ passe\ \:\ (.*)'
    m = re.search(pattern, text)

    return m.group(1)

def main():

    print 'Password: %s' % ch02()


if __name__ == "__main__":
    main()
