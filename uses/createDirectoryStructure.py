#!/usr/bin/env python

# This code is under BSD 2-clause license

import os
from random import *
from tempfile import *

fileSuffix=[
".txt",
".sh",
".doc",
".xml"
]

fileContents=[
"Ace of spades",
"Queen of hearts",
"King of clubs",
"Jack of diamonds",
"World of glass",
"Wildhoney",
"New year's day",
"Jackie",
"Sinead",
"Outer limits"
]

def CreateFile():

    randIndex = randrange( len(fileSuffix) )
    tempFile = NamedTemporaryFile(delete=False,dir='.',prefix='testfile-',suffix=fileSuffix[randIndex],mode='wt')
    # fill the file contents

    randIndex = randrange( len(fileContents) )

    contents = fileContents[randIndex]
    tempFile.file.write(contents)

    tempFile.close()
    return tempFile.name

def CreateDir():
    # creates a dir in current directory
    return mkdtemp(dir='.',prefix='testdir-')


def CreateTreeStructure(minFilesPerDirectory,maxFilesPerDirectory,minDirs,maxDirs,depthLevel):

    if depthLevel <= 0:
        return

    nFiles = randrange(minFilesPerDirectory,maxFilesPerDirectory)

    for i in range(nFiles):
        CreateFile()

    nDirectories = randrange(minDirs,maxDirs)

    directoryList = []

    for i in range(nDirectories):
        directoryName = CreateDir()
        directoryList.append(directoryName)

    for directory in directoryList:
        os.chdir(directory)
        CreateTreeStructure(minFilesPerDirectory,maxFilesPerDirectory,minDirs,maxDirs,depthLevel-1)
        os.chdir('..')

depthLevel = 4
minDirs = 2
maxDirs = 4

minFilesPerDirectory = 1
maxFilesPerDirectory = 3

root = CreateDir()
os.chdir(root)

CreateTreeStructure(minFilesPerDirectory,maxFilesPerDirectory,minDirs,maxDirs,depthLevel)
