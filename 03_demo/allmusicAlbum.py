#!/usr/bin/env python
# This code is under BSD 2-clause license

import sys

# hack to have the typical directory in the python import path
sys.path.append('../02_typical')

from getWebPageContents import *

def FixAllmusicXML(data):
    # check the invalid xml
    data = data.replace('itemscope','itemscope="dummy"')
    data = data.replace('&','')

    pos = data.find('<meta')
    while pos > 0:
        pos2 = data.find('>',pos)
        if data[pos2-1] != '/':
            data = data[:pos2]+'/'+data[pos2:]
        pos = data.find('<meta',pos2)

    return data

def ExtractAlbumFromAllmusicPage(html):
    start = '<tbody>'
    end = '</tbody>'
    startIndex = html.find(start)
    endIndex = html.find(end) + len(end)

    data = html[startIndex:endIndex]
    xmlValidData = FixAllmusicXML(data)
    return xmlValidData

def PrintAlbumInfoFromXMLData(xmlData):
    dom = parseString(xmlData)
    tdTags = dom.getElementsByTagName("td")

    for td in tdTags:
        if "tracknum" == td.getAttribute("class"):
            trackNumber = td.firstChild.nodeValue.strip()

        if "title-composer" == td.getAttribute("class"):
            songTitle = td.getElementsByTagName("a")[0].firstChild.nodeValue.strip()

        if "time" == td.getAttribute("class"):
            duration = td.firstChild.nodeValue.strip()
            print trackNumber + " " + songTitle + " " + duration

albumUrl = 'http://www.allmusic.com/album/wildhoney-mw0000940313'

html = GetWebPageContents(albumUrl)
xmlData = ExtractAlbumFromAllmusicPage(html)
PrintAlbumInfoFromXMLData(xmlData)
