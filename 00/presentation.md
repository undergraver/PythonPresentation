# About Python

Python is an interpreted programming language. That means you cannot execute the python code you've written if you don't have Python installed. In order to install it go to https://www.python.org/downloads/ and select the version you desire. 
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

## Command line arguments

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

