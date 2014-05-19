#!/usr/bin/env python
# This code is under BSD 2-clause license

place=["first", "second", "third"]
ranking=["Conrad","Jane","Fred"]

# list comprehension
diplomaTexts = [ ranking[i] + " was " + place[i] for i in range(len(place)) ]

for diplomaText in diplomaTexts:
    print(diplomaText)

print 40*"*"

# map with a lambda function
rankingWithBulletPoints = map(lambda x:'* '+x,ranking)
for singleRank in rankingWithBulletPoints:
    print(singleRank)

print 40*'_'

numbers = [1,2,3,4,5]

# reduce with a lambda function
sum_of_numbers=reduce(lambda x,y:x+y,numbers)
print( "Sum of " + str(numbers) + " is "+str(sum_of_numbers) )

# another map with a lambda function
square_values = map(lambda x:x*x, numbers)
print( "squares for " + str(numbers) + " are " + str(square_values) )

def IsOdd(num):
    return (num % 2) is not 0

# filter with a defined function
odd_filtered=filter(IsOdd,numbers)

print("Odd numbers filtered from " + str(numbers) + " are " + str(odd_filtered))

# list comprehension with condition
maxValue=10
filtered_squares = [ s for s in square_values if s < maxValue ]
print("Square values less than "+str(maxValue)+" are " + str(filtered_squares))
