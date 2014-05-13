#!/usr/bin/env python

# This code is under BSD 2-clause license

pythonRecipies=["Egg", "Bacon", "Sausage", "Spam"]

# append one more
pythonRecipies.append("Baked Beans")

print "How many recipies?"
print "We have " + str( len(pythonRecipies) ) + " recipies:"

for recipe in pythonRecipies:
    print(" - "+recipe)

print(40 * "-")

print "3 zeros:"
print (3 * [0])

print("What was the last one?")

# printf style format specifiers can be used
print("  %s" % (pythonRecipies[-1]) )

print("And the first one?")
print "  " + pythonRecipies[0]

# array slices (same thing works for strings)
print("Now the first two?")
print "  %s" % pythonRecipies[:2] # same as [0:2]

print("And now the last two?")
print "  %s" % pythonRecipies[-2:]

print("And the middle ones?")
print "  %s" % pythonRecipies[1:4]
