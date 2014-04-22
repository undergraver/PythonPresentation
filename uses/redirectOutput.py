#!/usr/bin/env python

# This code is under BSD 2-clause license

import subprocess

f = open('output_redirect.txt','wt')
subprocess.call('dir',stdout=f,shell=True)
f.close()
