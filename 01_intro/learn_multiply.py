#!/usr/bin/env python

import random

def ask_for_answer():
    num1 = random.randint(2,9)
    num2 = random.randint(2,9)
    try:
        answer = raw_input("%d x %d=" % (num1, num2))
    except EOFError:
        return None

    try:
        val = int(answer) 
    except:
        val = None

    result = num1*num2

    if val is not result:
        print("Wrong answer. Should be:"+str(result))
    else:
        print("Correct")

    return result

def main():
    while True:
        answer = ask_for_answer()
        if answer is None:
           break 


if __name__=="__main__":
    main()
