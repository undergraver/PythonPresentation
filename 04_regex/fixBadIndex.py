#!/usr/bin/env python

# This code is under BSD 2-clause license

import re

f = open('bad_index.c','rt')
lines = f.readlines()
f.close()

regex = r"changeValue\s*\(\s*(\d+)\s*,"
compiledRegex = re.compile(regex)
if compiledRegex is None:
    print "Invalid regex"

for line in lines:
    line = line[:-1]
    found = compiledRegex.search(line)
    if found is not None:
        # correct the index
        badIndexVal  = int(found.group(1))
        correctIndexVal = badIndexVal - 1

        # position in the string
        start = found.start(1)
        end = found.end(1)
        print(line[:start]+str(correctIndexVal)+line[end:])
    else:
        print(line)
