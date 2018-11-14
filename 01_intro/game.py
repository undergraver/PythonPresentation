#!/usr/bin/env python

import random

minVal=0
maxVal=200


def main():
    numberToGuess = random.randint(minVal,maxVal)
    print("Computer has generated a number between %d and %d. Guess that number!" % (minVal,maxVal))

    numberOfTries = 0
    done = False

    while not done:

        try:
            currentNum = int(input(""))
        except:
            break

        numberOfTries = numberOfTries + 1

        if currentNum == numberToGuess:
            done = True
            continue

        if currentNum < numberToGuess:
            print("Number too small")
        else:
            print("Number too big")

    if done:
        print("Well done! You guessed the number after %d attempts." % (numberOfTries))

if __name__=="__main__":
    main()


