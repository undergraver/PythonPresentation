#!/usr/bin/env python

# This code is under BSD 2-clause license

from os import path
import sys
from random import *

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
