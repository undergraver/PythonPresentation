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
