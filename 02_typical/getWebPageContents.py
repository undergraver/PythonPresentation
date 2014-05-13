#!/usr/bin/env python

# This code is under BSD 2-clause license
from xml.dom.minidom import parse, parseString
from xml.parsers import expat

import urllib2

def GetWebPageContents(url):
    response = urllib2.urlopen(url)
    html = response.read()
    return html

if __name__=="__main__":
    url = 'http://www.allmusic.com/album/wildhoney-mw0000940313'
    html = GetWebPageContents(url)
    print html
