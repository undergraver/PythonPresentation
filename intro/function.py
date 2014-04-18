#!/usr/bin/env python

# This code is under BSD 2-clause license

import random

def PickUpThePhone():
    # initialize the seed so we don't get
    # the same value each time the script runs
    random.seed()

def Dial(number):
    print("Dialing %s ..." % number)
    busy = random.randint(0,1) > 0
    if busy:
        print "... busy number"
    else:
        print "Hi honey ... feeling lonely?"


PickUpThePhone()

hotline="8989"

Dial(hotline)
