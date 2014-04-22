#!/usr/bin/env python

# This code is under BSD 2-clause license

import os
import sys

def ScanDir(dirName):
    fileNameList = os.listdir(dirName)

    for fileName in fileNameList:
        fullPath = os.path.join(dirName,fileName)
        if os.path.isdir(fullPath):
            ScanDir(fullPath)
        else:
            print fullPath


if len(sys.argv) < 2:
    print "Please provide the directory to scan as command line argument"
    sys.exit(1)

ScanDir(sys.argv[1])
