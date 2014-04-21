#!/usr/bin/env python

# This code is under BSD 2-clause license

import subprocess
import sys

folder=None
if len(sys.argv) > 1:
    folder = sys.argv[1]
else:
    print "Provide the HG repository location as command argument"
    sys.exit(1)

command = 'cd "%s" && hg id -i' % (folder)

revision='Command execution error'
try:
    revision = subprocess.check_output(command,shell=True)
except:
    pass

print "Current revision of HG repository found at '%s' is: %s" % (folder,revision)
