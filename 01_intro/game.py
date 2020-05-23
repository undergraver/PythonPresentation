#!/usr/bin/env python

import random
import sys

minVal=0
maxVal=1000

def print_msg(msg):
    sys.stdout.write(msg+"\r\n")
    sys.stdout.flush()

def print_err(msg):
    sys.stderr.write(msg+"\r\n")
    sys.stderr.flush()

def print_all(msg):
    print_msg(msg)
    print_err(msg)

def main():
    numberToGuess = random.randint(minVal,maxVal)
    print_msg("Computer has generated a number between %d and %d. Guess that number!" % (minVal,maxVal))

    numberOfTries = 0
    done = False

    while not done:

        try:
            currentNum = int(raw_input(""))
        except Exception as e:
            break

        numberOfTries = numberOfTries + 1

        if currentNum == numberToGuess:
            done = True
            continue

        if currentNum < numberToGuess:
            print_msg("Number too small")
        else:
            print_msg("Number too big")

    if done:
        msg = "Well done! You guessed the number %d after %d attempts." % (currentNum,numberOfTries)
        print_err(msg)

if __name__=="__main__":
    main()


