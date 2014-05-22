#!/usr/bin/env python

# This code is under BSD 2-clause license

import re

def smartReplace(match):
    badIndex = int(match.group(1))
    goodIndex = badIndex-1
    return 'changeValue('+str(goodIndex)+','

f = open('bad_index.c','rt')
lines = f.readlines()
f.close()

regex = r"changeValue\s*\(\s*(\d+)\s*,"
compiledRegex = re.compile(regex)
if compiledRegex is None:
    print "Invalid regex"

for line in lines:
    line = line[:-1] # remove the newline
    line = compiledRegex.sub(smartReplace,line)
    print line
