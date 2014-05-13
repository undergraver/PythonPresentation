#!/usr/bin/env python

# This code is under BSD 2-clause license

import sys

MY_CONSTANT=42

print __name__

def doStuff(argument):
    print "Working on " + argument

if __name__== "__main__":
    print "Script called directly"
    
    if len(sys.argv) < 2:
        print "Need 1 argument"
        sys.exit(1)
        
    argument = sys.argv[1]
    doStuff(argument)
    
else:
    print "Someone imported '" + __name__ + "'"
