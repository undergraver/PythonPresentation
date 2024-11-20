# References
* https://www.w3schools.com/python/default.asp
* https://docs.python.org/3/tutorial/
* https://docs.python.org/3/reference/

# About Python

Python is an interpreted programming language. That means you cannot execute the python code you've written if you don't have Python installed. 

## Installing Python
In order to install it go to https://www.python.org/downloads/ and select the version you desire. 
* For Windows you select the latest version, launch installer, make sure Python is in PATH (option from the installer) and put it in a shorter path like "C:\Python\Python313" instead of the default one (inside your user directories)
* For Linux you should prefer to get it from your distribution's repository.

# Python Interpreter

This is an executable capable of running Python code but it can also be used interactively - that means user can type python code inside of it and get results. To launch the interpreter
* in Windows: Start->Run "python" + OK
* in Linux: execute python / python3 from your shell (bash)

Example:
```
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x=1
>>> y=2
>>> x+y
3
>>> print(x)
1
>>> 78*34
2652
>>> 2+2/2
3.0
>>>
```

As you can see basic operation like addition (+) or multiplication (*) are quite intuitive and you can use Python as an advanced calculator as it knows pretty well the order of operations.

# Language basics
## Builtin data types
Full documentation can be found here: https://docs.python.org/3/library/stdtypes.html but we'll only mention some of them for simplicity and to get you started.
The full documentation should be accessed in case some special operations are required.
### Numeric types: Int/Float
No need for many comments here:
```
>>> x=1
>>> y=2.0
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> y*3
6.0
>>> x+y
3.0
>>>
```
### Boolean
These are variables that can be true or false. In python they are simply defined via True and False.
```
>>> x=False
>>> y=True
>>> type(x)
<class 'bool'>
>>> type(x)
<class 'bool'>
```

### Dictionary
Is a key-value pair of data structure.
First is the key, second is the value. In the example below, "city", "country" and "age" are keys, and they associates are values.
```
>>> d={'city':'London','country':'UK','age':1000}
>>> d
{'city': 'London', 'country': 'UK', 'age': 1000}
>>> d['city']
'London'
>>> d['age']
1000

```

### String
It's a basic container which stores characters - it can be considered as an array of characters. It's actually text that appears everywhere. Full docs: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
You can do many operations like add string to another string.

Example:
```
>>> s1="I salute"
>>> s2="you"
>>> s1+s2
'I saluteyou'
>>> s1+" "+s2
'I salute you'
>>>
```
### List
It is a container that can host multiple elements, not necessarily of the same type.
Exagerated example, storing the previous types in a list (comments are after # and are present here for documentation purpose):

```
>>> l = [] # empty list
>>> len(l) # should be zero
0
>>> l.append(1.0)
>>> l.append(101)
>>> l.append("my string")
>>> l
[1.0, 101, 'my string']
>>> print(l)
[1.0, 101, 'my string']
>>> "potato,plum,cherry".split(',') # you can even split a string to obtain a list of strings
['potato', 'plum', 'cherry']
>>>
```

This can be continued with some more comprehensive documentation found here: https://docs.python.org/3/tutorial/datastructures.html (there are also other data structres presented there)

We can access elements by their position but keep in mind that the first element has index 0, just like in the next example:
```
>>> l=[1.0, 101, 'my string']
>>> l[0]
1.0
>>> l[1]
101
>>> l[2]
'my string'
>>> l[3]
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    l[3]
    ~^^^
IndexError: list index out of range
>>>
>>> l[-1]
'my string'
>>>
```

Python also offers for convenience negative indices like "-1" index for the last element but we need to be careful when using those:
```
>>> l[-1]
'my string'
>>> l[-2]
101
>>> l[-3]
1.0
>>> l[-4]
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    l[-4]
    ~^^^^
IndexError: list index out of range
>>>
```

We can also get parts of the array via the "slicing" notation. For example returning a slice of the list without the first element is done like this:
```
>>> l = [1,2,3,4,5,6,7,8]
>>> l[1:]
[2, 3, 4, 5, 6, 7, 8]
```

```
>>> l[0:2] # elements between index 0 and index 2 (not including), that is index 0 and 1
[1, 2]
>>> l[:2]  # elements until index 2 (the same as above)
[1, 2]
>>> l[1:8:3] # elements from index 1, until 8 with a step of 3
[2, 5, 8]
>>> l[0:8:3] # elements from index 0, until 8
[1, 4, 7]
>>>
```
Further documentation: https://docs.python.org/3/library/functions.html#slice

## Modules
Modules can be seen as toolboxes with various tools inside of them. Those tools can be functions, classes or even other (sub)modules. For the moment we're looking at some modules that come with the normal Python distribution. One of these modules is the math module containing various mathematical functions like sqrt and pow. We can use the "import" keyword to be able to use the module.
```
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
>>> help(math.gcd)
Help on built-in function gcd in module math:

gcd(*integers)
    Greatest Common Divisor.

>>> 
```
We can even test some of these functions:
```
>>> math.pow(2,3)
8.0
>>> math.sqrt(3)
1.7320508075688772

```
Another way of using the module is to use the "from MODULE import ..." syntax just like in the next 2 examples:
```
>>> from math import pow
>>> pow(6,2)
36.0

```

```
>>> from math import *
>>> cos(3.14)
-0.9999987317275395
>>> sin(1.57)
0.9999996829318346
>>> 

```
Want to go deep? Mariana Trench is a joke compared to amount of tutorials you can find online. Start here: https://docs.python.org/3/tutorial/modules.html

## Elements of structured programming

### Functions
We've seen previously that we had code with functions like "print", "pow", "cos" etc. These functions can even return values even that is not always necessarily.
```
>>> import math
>>> ret = math.pow(2,4)
>>> print(ret)
16.0
>>> type(ret)
<class 'float'> # this means pow returns a float
>>> val = print('test')
test
>>> type(val)
<class 'NoneType'> # the print function doesn't return anything
>>>
```

But you can also write your own functions that being a  first step towards structured programming.

Since you will not use python in the interpreter in most of the cases so you will need to write the code into a file. When doing this, most likely you will start making functions to avoid rewriting code multiple times.
In this case we use the "Idle" editor that comes with Python (not the only one that can be used) out of commodity but we should switch in time to more complex editors with more optoins.

Example:
```
def half_square(number):
    # number is the only parameter of this function
    value = number*number
    value = value / 2
    return value

#### - please remark the indentation (4 spaces in this case, but it also can be 2 spaces, a TAB etc - the idea is to have it consistent inside a single file)

v = half_square(6)
print(v)
v = half_square(7)
print(v)

```

Using functions makes the code reusable/easier because you stop repeating the same procedures again in different parts of code, replacing this with a simple call. The functions receive one or more parameters; in our case there was only one but we can write functions receiving multiple parameters, even **variable number of parameters** if that's desired.

### Conditional statements

This chapter tells you how write conditional code, that is code that depends on specific conditions. This is done via the **if** statement, following the same indentation found in the case of functions. We're going make use of a module called random which will provide us with pseudo-random numbers - more on this topic here: https://docs.python.org/3/library/random.html

```
import random

lab = random.randint(3,10) # an integer between 3 and 10, including 3 and 10
exam = random.randint(3,10)

# NOTE: Comments with multiple # are here to show how indentation works

if lab >= 5:
    if exam >= 5:
        print("You passed.")
        
####
    #### - under this if

    else:
        print("You qualified for the exam but failed.")

####
    #### - under this else


#### - under the first if
    s = "Lab grade was {0} and exam grade was {1}.".format(lab, exam)
    print(s)

else:
    print("You failed to qualify for the exam.")
    # see https://docs.python.org/3/library/string.html#formatstrings
    # for more information about formatting strings (quite a lot of reading)
    dynamicString = "Your lab grade was {0} which is below 5.".format(lab)
    print(dynamicString)

```

But beside if/else we also have elif (else if) which can make multiple conditions inside your code. For example we want to know if a number is between two numbers. For this we'll read the data as user input (standard input, stdin or console is the word, depending on your environment).

```
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

```

### Loops

Loops are a way to iterate through sets of data. We'll show a simple example printing each part of a string after we split it.
```
my_string = "apples,organges,figs,mushrooms"
fruits = my_string.split(',') # we split after "," separator

# it iterates through a list
for f in fruits:
    print(f)

# we can also iterate based on a counter

counter = 0
# while the condition is true this repeats
while counter < 10:
    print(counter)
    # failure to increment the value results in an infinite loop; try it
    counter = counter + 1

# isn't it cool you can multiply strings?
print('+'*80)

for n in range(10):
    print(n)
```

Most of the time you need to play little with everything to be familiar.

You can also check the "range" object which returns an iterable entity that can be displayed with a for. In the example above you can see it as the last example.

All these can be learnt at your own pace with additional information from https://docs.python.org/3/tutorial/introduction.html

If you really want to go into more details start here: https://docs.python.org/3/tutorial/

**Make sure you attain the proper language used in python programming.** This will be the most important thing because you will need to search for issues on the interwebs and without the proper framing you will most likely end up in areas that will waste your time.

## Classes

Classes are way to define actual objects in Python. The theory and options behind this is quite big but we'll have some examples in order to understand what we are talking about. We already used classes in our examples. For example a list is a class, an integer is also a class, a float is a class etc. It is always an interesting thing to type help with the particular class to find out more info about it. For example here I found out about bit_count and bit_length which are quite interesting functions. For these functions there are a lot of functions starting with `__` like `__add__` which is actually how the `+` operator performs. 

```
>>> x=4
>>> y=1.1
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> help(x)
Help on int object:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
....
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |
 |      Also known as the population count.
 |
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
```

Those functions can actually be called on an integer instance.
```
>>> x=4 # 100 in binary
1
>>> x=7 # 111 in binary
>>> x.bit_count()
3
>>>
```

We will not go to deep, but stick to basic stuff, leaving an idea on how they can be used.
As an example we'll show some of the properties of a city with the help of a class. 
```
class City:
    # this is a special function called a constructor
    # it receives 3 parameters (the self parameter is
    # a reference to the class instance)
    def __init__(self,name,country,population):
        self.name = name
        self.country = country
        self.population = population

    # this is a function that describes the contents as string
    # more info here: https://docs.python.org/3/reference/datamodel.html#object.__str__
    def __str__(self):
        s = "{0} from {1} with a population of {2}"
        return s.format(self.name, self.country,self.population)

    # this is absurd, it's only for demo
    # more here: https://docs.python.org/3/reference/datamodel.html#object.__add__
    def __add__(self,city):
        city_names = [self.name, city.name]
        newname = "+".join(city_names) # see join method of string
        city_countries = [self.country, city.country]
        newcountry = "/".join(city_countries)
        population = self.population + city.population
        return City(newname,newcountry,population)
        


p = City("Paris","France",11000000)
l = City("London","UK",9000000)

print(p)
print(l)

print(p+l)

print(p.name)
print(l.population)
print(l.country)

```
In the example above we could get rid of `__add__` and `__str__` if we're not interested in displaying the class as string (or adding them) but rather use it as a property bundle, that being 100% correct. To access the class members you can simply use the `.` like shown above in the last lines.

Go for more information here: https://docs.python.org/3/tutorial/classes.html.

## Reading/Writing to files

Most of the programs need to interact with the environment in which they are executed for different purposes like
- reading input data which is difficult to pass from user input
- writing results of operations which could be the input for other programs

Note: In this section we will concentrate on writing text files which are very easy to understand. This doesn't include writing formatted text files like XML (via https://docs.python.org/3.13/library/xml.etree.elementtree.html ) even though they are still text files.

### Reading
We will offer a simple example on how to read data from a file named "vote_count.txt". This file should contain integers that are separated by space, new lines, tabs etc so that we can obtain the entire list with a simple "split" operation as described in the help:
```
>>> help(str.split)
Help on method_descriptor:

split(self, /, sep=None, maxsplit=-1) unbound builtins.str method
    Return a list of the substrings in the string, using sep as the separator string.

      sep
        The separator used to split the string.

        When set to None (the default value), will split on any whitespace
        character (including \n \r \t \f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits.
        -1 (the default value) means no limit.

    Splitting starts at the front of the string and works to the end.

    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.
>>>
```
The final result of the reading should be the sum of all integers printed on the screen.

For opening a file we have the "open" which is a Python built-in function which returns an object through which we can perform operations on that file (reading in this case)

```
>>> f = open("members-os4k-ro.csv","rt")
>>> dir(f)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
>>> type(f)
<class '_io.TextIOWrapper'>
>>>
```

To read everything from a file in a string you can use the read() function which with default parameters will read entire file and return a string with it:
```
>>> help(f.read)
Help on built-in function read:

read(size=-1, /) method of _io.TextIOWrapper instance
    Read at most size characters from stream.

    Read from underlying buffer until we have size characters or we hit EOF.
    If size is negative or omitted, read until EOF.

>>>
```

After the file is no longer needed best practice is to close it (via close function). All files will be closed when program exits but if your programs makes a lot of operations that involve reading many files it might turn out you're going to be out of resources at some point.

```
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    f.read()
    ~~~~~~^^
ValueError: I/O operation on closed file.
>>> 
```

Once a file is closed any operation on it will fail by throwing an exception; exceptions and their handling will be discussed later.

Only the first three lines are relevant to this chapter, the rest being already presented before.

```
f = open("vote_count.txt","rt") # r - is for reading, t - is for text (even if it's implicit - see help for more)
buf = f.read() # this reads the entire file and put it into bug
f.close() # we close the file as we no longer need it

split_integers_as_strings = buf.split()
# after this operation we have a list of integers each as string

#print(split_integers_as_strings)

sum = 0
for int_str in split_integers_as_strings:
    int_value = int(int_str) # convert from string to int
    sum = sum + int_value

print(sum)

```

### Writing

We will extend the previous code to write the final result inside another text file named "total_votes.txt" that should contain only one integer on a line, representing the sum of those integers.

As you might guess writing files is very similar to what we described before so the example comes with no explanation but as an append at the previous example:
```
f = open("vote_count.txt","rt") # r - reading, t - text (implicit); check help!
buf = f.read() # this reads the entire file and put it into bug
f.close() # we close the file as we no longer need it

split_integers_as_strings = buf.split()
# after this operation we have a list of integers each as string

#print(split_integers_as_strings)

sum = 0
for int_str in split_integers_as_strings:
    int_value = int(int_str) # convert from string to int
    sum = sum + int_value

print(sum)

f = open('total_votes.txt',"wt")
sum_as_str = str(sum)
f.write(sum_as_str)
f.close()

```

## Special text file formats

Previously we've seen how to write simple text files. However in normal day to day use operating systems use a ton of specially formatted text files for various purposes:
* configuration of programs, settings
* exchange information across various environments (Internet, network, file system etc)

The advantage of text file format is that they can be easily read by human eye and you can easily perform changes to them, if required. We're going to examine next some of the most used text file formats together with examples, references.

### XML file format
The xml file format is a way of storing data between tags. Using this way of storing information. Documentation about the format: https://en.wikipedia.org/wiki/XML

### JSON file format
The json format is very used when it comes to web services. It is preferred because it is easily digestable from Java Script, which is heavily used in modern web application. Even its name comes from that particular usage as you can see from the documentation: https://en.wikipedia.org/wiki/JSON

Reading and writing XML in python is done via some embedded modules, namele the `json` module.
In the next sections we'll only show the samples with comments where required. They can also be found in the repository under `json_examples` directory.

Documentation used for the examples: https://docs.python.org/3/library/json.html
#### Reading JSON
```
import json

# this reads json from file directly
#with open('example.json', 'r') as file:
#    data = json.load(file)

# this will read the file contents and use loads
# to load the json contents

f = open('example.json','r')
buf = f.read()
f.close()

data = json.loads(buf)

print("Name:"+data['first_name'])
print('Age:'+str(data['age']))
print('Height:'+str(data['height']))
print('Children:'+str(data['children']))

print(data['phone_numbers'][0]['number'])

phoneNumbers = data['phone_numbers']
print("Phone numbers:")
for phone_number in phoneNumbers:
    print("{0} number is {1}".format(phone_number['type'],phone_number['number']))


# Print the data
#print(data)

```

#### Writing JSON
```
import json

my_json={   "car":"dacia","age":16,
            "functional":False,"attributes":[
                {"capacity":1190},
                {"power":100},
                {"model":"logan"}
                ]}

with open('json_written.json','wt') as f:
    json.dump(my_json,f,indent=4)

# note: indent parameter helps with a nice formatting
# if indent wouldn't be specified (left with the default values)
# the json would be written on a single line - same information, but less human readable
#
# please check
```

### INI file format
it is mostly used for configuration files, especially under Windows as registry configuration files. In Python the ini files can be accessed via the configparser module. See here for more details: https://docs.python.org/3/library/configparser.html

Extra info: https://en.wikipedia.org/wiki/INI_file

### CSV file format
It is a format for storing column based data (just like Excel or similar applications).
This will be discussed in the practice section more. Make sure you check that section if needed.

## Command line arguments

In the previous two example we've seen that the names of the files are written inside the python scripts. That is good for learning/testing but in real life it might be that we have multiple files whose names are not known that should be processed making it very difficult for these programs to be extendable. In such cases a very good option is to pass the files we want to process at command line. This is a very used thing in Unix environment where command line tools are extremely powerful. For example we can search for a particular string in multiple files and we can use the **cat** and **grep** commands.

Unix example on how command line parameters work:
```
# file1 file2 file3 are command line arguments to "cat" command
# python is a command line argument to "grep" command
cat file1 file2 file3 | grep python # we find out if python can be found in these 3 files
```
As you might imagine we will expand the example that we have in order to perform the sum (from reading section) on multiple files. The way Python offers to us the arguments is via the sys.argv string list (from the sys module offered by Python).

A simple example and how to run it:

Code:
```
import sys
print(sys.argv)
```

How to execute it (sensitive data was removed):
```
c:\Users\Downloads\source\00>007_args.py
['C:\\Users\\Downloads\\source\\00\\007_args.py']

c:\Users\Downloads\source\00>007_args.py 1 2 3 4 5
['C:\\Users\\Downloads\\source\\00\\007_args.py', '1', '2', '3', '4', '5']

c:\Users\Downloads\source\00>
```

As we can see the first argument is the name of the python script (index 0) and the second (index 1) is the first actual param and so on. 

Based on this we will extend the example from the reading phase to be able to handle each file. This implies some small refactoring to avoid duplicate code which is accepted in code meant for educational purposes but not in production.

This code is a more structured version of the initial one:
```
import sys

def count_votes(file_name):
    f = open(file_name,"rt")
    buf = f.read() # this reads the entire file and put it into bug
    f.close() # we close the file as we no longer need it

    split_integers_as_strings = buf.split()
    # after this operation we have a list of integers each as string

    #print(split_integers_as_strings)

    total = 0
    for int_str in split_integers_as_strings:
        int_value = int(int_str) # convert from string to int
        total = total + int_value

    return total

total_votes = 0
file_list = sys.argv[1:] # eliminate the first element
for fname in file_list:
    total_votes += count_votes(fname)

print("Total votes in:"+str(file_list)+":"+str(total_votes))
```

Executing it gives us the following output:
```
c:\Users\Downloads\source\00>008_command_line.py vote_count.txt
Total votes in:['vote_count.txt']:15

c:\Users\Downloads\source\00>008_command_line.py vote_count.txt vote_count.txt
Total votes in:['vote_count.txt', 'vote_count.txt']:30

c:\Users\Downloads\source\00>008_command_line.py vote_count.txt vote_count.txt vote_count.txt
Total votes in:['vote_count.txt', 'vote_count.txt', 'vote_count.txt']:45

c:\Users\Downloads\source\00>
```

### Deeper dive for command line arguments
Command line arguments can be extended to offer many options to the programs we're making. If we go back to unix functions we can find from their manual (man grep) they have a lot of options. For example grep can be case insensitive in their search when passing the -i argument.
```
man grep excerpt
...
       -i, --ignore-case
              Ignore case distinctions, so that characters that differ only in
              case match each other.
...
```

So when issueing this command grep will search also for Python, PYTHON, pYTHon etc, not only for python
```
cat file1 file2 file3 | grep -i python
```

This can be achieved via the argparse module https://docs.python.org/3/library/argparse.html from python. We will not cover this here.

## Exceptions and their handling

The computer is not the place where everything works every time as expected. For example:

- we can try to write a file and the disk is full
- we are trying to access a web site and the internet connection fails
- we try to open a file and the file cannot be access (doesn't exist or we have no rights to create the file in that particular directory)
- we make a division by 0 because we haven't validated the data.
- ...

When such exception are raised the program will exit if the are not handled. Sometimes this is a good thing, but if we can handle those exceptions we should do that and leave the program running forward.

Example of code uncaught exception and the output in few scenarios:
```
s1 = input("dividend:")
s2 = input("divisor:")

f1 = float(s1)
f2 = float(s2)

res = f1/f2

print("The result is:"+str(res))
```

As we can see in the first case the code stops when the exception is happening because of the exception.

```
c:\Users\Downloads\source\00>009_exception_not_caught.py
dividend:3
divisor:0
Traceback (most recent call last):
  File "C:\Users\Downloads\source\00\009_exception_not_caught.py", line 7, in <module>
    res = f1/f2
          ~~^~~
ZeroDivisionError: float division by zero

c:\Users\Downloads\source\00>009_exception_not_caught.py
dividend:3
divisor:2
The result is:1.5

c:\Users\Downloads\source\00>
```

To prevent this we should rewrite the code to handle the exceptions in some parts of code just like in the next example:
```
s1 = input("dividend:")
s2 = input("divisor:")

f1 = float(s1)
f2 = float(s2)

try:
    res = f1/f2
#except: # < we can use this method if don't want cathing the exception
except Exception as e:
       print("Exception caught:"+str(e))
       res = "Invalid input"

print("The result is:"+str(res))
```

Output is:
```
c:\Users\Downloads\source\00>009_exception_caught.py
dividend:3
divisor:0
Exception caught:float division by zero
The result is:Invalid input

c:\Users\Downloads\source\00>009_exception_caught.py
dividend:3
divisor:4
The result is:0.75

c:\Users\Downloads\source\00>
```

We can also raise exceptions from our code but that is not going to be presented here. For more details about exceptions please visit this page: https://docs.python.org/3/tutorial/errors.html


# Asking for help
Usually you can search the online help via your search engine and it will **usually** get you somewhere under this domain: https://docs.python.org/
You can also search for help in the interpreter via the help command
```
>>> import math
>>> help(math.pow)
Help on built-in function pow in module math:

pow(x, y, /)
    Return x**y (x to the power of y).

>>>
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to 'utf-8'.
 |  errors defaults to 'strict'.
 |
 |  Methods defined here:
....
```
When you don't know what an object/class contains you can use `dir`
```
>>> help(dir)
Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings

    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.

>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>>
```

There you can find a list of exposed methods available on str and you can even test them.

```
>>> name="Zappa"
>>> name.upper()
'ZAPPA'
>>> name.lower()
'zappa'
>>> name.swapcase()
'zAPPA'
>>>
```

To find the type of an object you can use type:

```
>>> x=1
>>> city="Brasov"
>>> type(x)
<class 'int'>
>>> type(city)
<class 'str'>
>>>
```

Afterwards you can use the type with help/dir to find out more information about it.

