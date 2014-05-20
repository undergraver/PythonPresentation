#!/usr/bin/env python

# This code is under BSD 2-clause license

import re

f = open('names.txt','rt')
names = f.readlines()
f.close()

regex = r'[ \t]*([a-zA-Z]+)[ \t]+([a-zA-Z]+)[ \t]*'

compiledRegex = re.compile(regex)
if compiledRegex is None:
    print("Invalid regex")

for name in names:
    name = name.strip()
    m = compiledRegex.match(name)
    if m:
        #print m.group(1)
        #print m.group(2)
        swappedName = m.expand(r'\2 \1')
        print(swappedName)
    else:
        print("x"+name)
