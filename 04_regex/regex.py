#!/usr/bin/env python
# This code is under BSD 2-clause license

import re

text = 'Contact CompanySeven at : office7@gmail.com or sales7@gmail.com.uk!!'
print text
print '-' * 40

#split
regex = ' ' # split by space
result = re.split(regex, text)
print regex
print result
print '-' * 40

regex = '[  @:!]' # character group: split by space, @ or :
result = re.split(regex, text)
print regex
print result
print '-' * 40

regex = '[0-9]' # character group with range: split by any character from '0' to '9'
result = re.split(regex, text)
print regex
print result
print '-' * 40

regex = '[^a-zA-Z0-9]' # split by anything that is not a letter or a number
print regex
result = re.split(regex, text)
print result
print '-' * 40

regex = '[  @:!]+' # split by one or multiple consecutive delimiters
print regex
result = re.split(regex, text)
print result
print '-' * 40

# substitution
regex = '[a-zA-Z0-9_-]+@[a-zA-Z0-9_\\.-]*'

result = re.sub(regex, '<email address hidden>', text)
print regex
print result
print '-' * 40

# find all
regex = '[a-zA-Z0-9_-]+@[a-zA-Z0-9_\\.-]*'
result = re.findall(regex, text)
print regex
print result
print '-' * 40

regex = '([a-zA-Z0-9_-]+)@([a-zA-Z0-9_\\.-]*)'
result = re.findall(regex, text)
print regex
print result
print '-' * 40

# match with advanced information
regex = 'Contact ([a-zA-Z]+) at : (.*)!'
match = re.search(regex, text)
print regex
if match is None:
    print 'no match'
else:
    print match.groups()
    print 'Start: ' + str(match.start(0)) + ' ' + str(match.start(1)) + ' ' + str(match.start(2))
    print 'End: ' + str(match.end(0)) + ' ' + str(match.end(1)) + ' ' + str(match.end(2))
    print text[match.start(1):match.end(1)]
print '-' * 40

# substitution with callback
regex = '([a-zA-Z0-9_-]+)@([a-zA-Z0-9_\\.-]*)'

def obfuscate(match):
    user = match.group(0)
    domain = match.group(1)
    
    domain = domain.replace('.', ' dot ')
    return '[' + user + ' at ' + domain + ']'

result = re.sub(regex, obfuscate, text)
print regex
print result
print '-' * 40

# more regular expressions
text = '<body> hello </body>'
print text
print '-' * 40
regex = '<(.*)>' # * tries to match as much text as possible
match = re.search(regex, text)
print regex
print match.group(1)
print '-' * 40

text = '<body> hello </body>'
regex = '<(.*?)>' # *? tries to match as little text as possible
match = re.search(regex, text)
print regex
print match.group(1)
print '-' * 40

text = '23, -100, +100'
regex = '[+-]?[0-9]+' # ? means the previous match is optional
result = re.findall(regex, text)
print regex
print result
print '-' * 40

text = 'Mr George Louis Costanza , Jerry Seinfeld , Ms Benes'
regex = '([a-zA-Z ]+)'
result = re.findall(regex, text)
print regex
print result
print '-' * 40

regex = '\s*([a-zA-Z ]+)\s*'
result = re.findall(regex, text)
print regex
print result
print '-' * 40

regex = '\s*(Mr|Ms)?\s*([a-zA-Z ]+)\s*'
result = re.findall(regex, text)
print regex
print result
print '-' * 40

regex = '\s*(?:Mr|Ms)?\s*([a-zA-Z ]+)\s*'
result = re.findall(regex, text)
print regex
print result
print '-' * 40
