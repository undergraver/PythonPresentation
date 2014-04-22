#!/usr/bin/env python

import os

fileName = "test.txt"

# create a file (similar flags to 'fopen' function)
f = open(fileName,'wt')

f.write("Hello World,\n")
f.write("\n")
f.write("This is a Python example of how to manipulate files.\n")
f.write("\n")
goodByeStrings=["Happy coding,\n","Python Demo\n"]
f.writelines(goodByeStrings)

f.close()

# read the created file
f = open(fileName,'rt')

entireFileBuf = f.read()

print 80*'-'
print entireFileBuf
print 80*'-'

# go back to the begining of file
f.seek(0)

fileLines = f.readlines()

print fileLines

f.close()

# remove the file
try:
    os.remove(fileName)
    print "Removal of '%s' successfull" % (fileName)
except:
    print "Failed removing %s" % (fileName)
