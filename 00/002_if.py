low=5
high=10
# the next formatting is more difficult but if you really want to understand it
# go to this page https://docs.python.org/3/library/string.html#formatexamples
print("We will tell you if a number is between %d and %d." % (low, high))
string_value = input("Please enter your number:")
x = int(string_value) # transforms the string into an integer
if x < low:
    print("{0} is below {1}".format(x,low))
elif x > high:
    print("{0} is above {1}".format(x,high))
else:
    print("{0} is between {1} and {2}".format(x,low,high))
