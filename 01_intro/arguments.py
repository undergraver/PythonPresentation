#!/usr/bin/env python

# This code is under BSD 2-clause license

# optional, named arguments
def print_profile(user, city, name = "<Anonim>", age = None):
    print '-' * 40
    print user
    print city
    print name
    if age != None:
        print age
        
print_profile("birlic04", "Adjud")
print_profile("sandel_car", "Caracal", name = "Sandu")
print_profile("linda", "Rupea", age = 25)
print_profile("aurica", "Darste", age = 25, name = "Aurelia")

# return multiple values
def gpsPosition()
    return (45.655902, 25.610652, 415) # a tupple
    
pos = gpsPosition()
print pos

lat, long, alt = gpsPosition() # use tupple unpacking to assign each item to a variable
print lat, long, alt

# another way is to use dictionaries
