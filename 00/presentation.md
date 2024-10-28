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

## Functions
You will not use python in the interpreter in most of the cases so you will need to write the code into a file. When doing this, most likely you will start making functions to avoid rewriting code multiple times.
In this case we use the "Idle" editor that comes with Python (not the only one that can be used).
Example:
```
def half_square(number):
    value = number*number
    value = value / 2
    return value


v = half_square(6)
print(v)
v = half_square(7)
print(v)

```

Functions are the first step towards a structured program, where several operations can be used.

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


# Asking for help
Usually you can search the online help via your search engine and it will get you somewhere under this domain: https://docs.python.org/
You can also search for help in the interpreter via the help command
```
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

