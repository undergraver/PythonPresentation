#!/usr/bin/env python

# This code is under BSD 2-clause license

pythonRecipies=["Egg","Bacon","Sausage","Spam","Baked Beans"]

print "How many recipies?"
print "We have " + str( len(pythonRecipies) ) + " recipies:"

for recipe in pythonRecipies:
    print(" - "+recipe)

print(40 * "-")

print("What was the last one?")

# printf style format specifiers can be used
print("  %s" % (pythonRecipies[-1]) )

print("And the first one?")
print "  " + pythonRecipies[0]
