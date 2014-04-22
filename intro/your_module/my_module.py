#!/usr/bin/env python

# This code is under BSD 2-clause license

MY_CONSTANT=42

print __name__

if __name__=="__main__":
    print "Script called directly"
else:
    print "Someone imported '" + __name__ + "'"
