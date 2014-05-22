#!/usr/bin/env python

# This code is under BSD 2-clause license

import psutil

for proc in psutil.process_iter():
    print proc
