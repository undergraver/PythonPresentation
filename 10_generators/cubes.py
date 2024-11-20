#!/usr/bin/python

print("stack { 1^1 = 1 ")

num = 2

while True:
    square = num*num*num
    if square <= 1000:
        print("# {0}^3 = {1} ".format(num,square))
        num += 1
    else:
        break

print("}")
