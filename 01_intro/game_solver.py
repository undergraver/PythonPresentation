#!/usr/bin/env python
import sys

from game import *


def read_line_from_stdin():
    s = ''
    while True:
        c = sys.stdin.read(1)
        if c == '\n' or c == '':
            break
        s = s+c
    return s

headermsg = read_line_from_stdin() 

print_err(headermsg)

minVal=None
maxVal=None

msgparts = headermsg.split(' ')

for part in msgparts:
    try:
        val = int(part.strip('.'))
        if minVal is None:
            minVal = val
        elif maxVal is None:
            maxVal = val
            break
    except Exception as  e:
        pass

while True:
    middle = (minVal + maxVal) / 2
    print_msg(str(middle))
    msg=read_line_from_stdin()
    if msg.find('small') >= 0:
        # too small
        minVal=middle+1
    elif msg.find('big') >= 0:
        # too big
        maxVal=middle-1
    else:
        # well done
        print_err("number was "+str(middle))
        break
