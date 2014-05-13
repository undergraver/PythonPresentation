#!/usr/bin/env python
# This code is under BSD 2-clause license

# create a dictionary
tenerife = {
    'country': 'Spain', 
    'population': 908555, 
    'area': (442, 'km2')
}

# dictionaries are great for searching even with thousands of items

# add/change value
tenerife['population'] += 5
tenerife['timezone'] = 1

# get value
print tenerife['country']

# iterate
print '--- keys, values'
for key, value in tenerife.items():
    print str(key) + ' => ' + str(value)
    
# iterate keys
print '--- keys'
for key in tenerife.keys():
    print str(key)

# iterate values
print '--- values'
for value in tenerife.values():
    print str(value)
    
# check key
if not tenerife.has_key('highest point'):
    tenerife['highest point'] = (3718, 'm')
    
# alternate check key (key not found exception)
print '--- vizits'
for i in range(3):
    try:
        tenerife['times visited'] += 1
        print 'Added 1 vizit'
    except KeyError:
        tenerife['times visited'] = 1
        print 'First vizit'
    print tenerife['times visited']
    
# in python there are no output parameters so, to return multiple items, you can create a class
# an easier alternative is to pack the values in a dictionary (or an array, but you will have no names)
import time
def currentTimeAndTimezone():
    now = time.time()
    tz = time.timezone
    return {'timestamp': now, 'time zone': tz}

timeAndTz = currentTimeAndTimezone()
print '--- currentTimeAndTimezone'
print timeAndTz
