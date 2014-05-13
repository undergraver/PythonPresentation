#!/usr/bin/env python

# This code is under BSD 2-clause license

from os import path
import sys
from random import *
from sys import argv as argument_list

# test imported from os
pathToCheck="."
if path.exists(pathToCheck):
    print "'%s' exists" % (pathToCheck)
else:
    print pathToCheck + " doesn't exist"

# test import from sys
print "Arguments: " + str(sys.argv)

# test import from random
seed()
print "A random number:" + str( random() )

# test import of sys.path
print 'argument_list is the same as sys.argv? ' + str(argument_list == sys.argv)
