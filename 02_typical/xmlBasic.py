#!/usr/bin/env python

# This code is under BSD 2-clause license

from xml.dom.minidom import parse, parseString


def handleDOM(document):
    examples = document.getElementsByTagName("example")
    for example in examples:
        handleExample(example)

def handleExample(example):
    name = example.getAttribute('name')
    print 40*'_'
    print "going through '%s' example" % (name)

    items = example.getElementsByTagName("item")
    for item in items:
        print item.firstChild.nodeValue

#dom = parse('./test.xml') # parse an XML file by name
contents="""\
<demo>
<example name="hello">
    <item>Say hello to xml!</item>
</example>
<example name="bye">
    <item>Always have a valid xml in mind!</item>
    <item>Good bye!</item>
</example>
</demo>"""

document = parseString(contents)

handleDOM(document)
