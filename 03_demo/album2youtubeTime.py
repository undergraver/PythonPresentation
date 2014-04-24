#!/usr/bin/env python
# This code is under BSD 2-clause license

import sys

import re
import sys

def LoadLines(fileName):
    f = open(fileName)
    lines = f.readlines()
    f.close()
    return lines

def SaveLines(fileName,lines):
    f = open(fileName,'wt')
    f.writelines(lines)
    f.close()

def ConvertDurationToSeconds(durationString):
    values = [int(val) for val in durationString.split(':') ]
    
    seconds = 0
    for value in values:
        seconds = seconds * 60
        seconds = seconds + value
        
    return seconds
    
def ConvertSecondsToDuration(seconds):
    values = []
    while seconds > 0:
        values.append( seconds % 60 )
        seconds = seconds / 60
        
    while len(values) < 2:
        # make it MM:SS
        values.append(0)
    
    strVal = ""
    for index in range(len(values)-1,-1,-1):
        strVal += ("%02d") % values[index]
        if index > 0:
            strVal += ":"
        
    return strVal

def ConvertLines(lines):
    convertedLines = []
    reg = re.compile(r"(.+)(\d+:-?\d+)")
    
    secondCounter = 0
    
    for line in lines:
        line = line.strip()
        matches = reg.match(line)
        if matches is not None:
            info = matches.group(1)
            duration = matches.group(2)
            newLine = info + ConvertSecondsToDuration(secondCounter) + "\n"
            secondCounter += ConvertDurationToSeconds(duration)
            convertedLines.append(newLine)
        else:
            convertedLines.append(line + "\n")
            
    return convertedLines
    
if len(sys.argv) < 2:
    print "Please provide the file with the album description"
    sys.exit(1)
    
inFileName = sys.argv[1]
outFileName = "output_" + inFileName

lines = LoadLines(inFileName)
newLines = ConvertLines(lines)
SaveLines(outFileName,newLines)

