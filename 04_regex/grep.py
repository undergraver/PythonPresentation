#!/usr/bin/env python

# This code is under BSD 2-clause license

import sys
import re

def grep(regex,fileName):
    regexCompiled = re.compile(regex)
    if regexCompiled is None:
        print "Invalid regex"
    
    f = open(fileName)
    lines = f.readlines()
    f.close()
    lineNumber = 1
    for line in lines:
        line = line.rstrip() # right strip
        if regexCompiled.search(line) != None:
            print str(lineNumber)+":"+line
        
        lineNumber = lineNumber + 1

# we open this file
this_file = sys.argv[0]
grep(r'print',this_file)
