# Problem
In company with 1000 employees HR needs to print papers for each employee sign.  Each of these papers are following a template where things like name, birth date etc are the only things that vary. The list of employees and their information is in a database kept in a CSV (Comma Separated Values) format. The template of the document is given as a text file with annotations like @@NAME@@ @@BIRTH_DATE@@ present so that we know what to replace with the actual values.

Steps:
- read data from csv in a class called Employee
- read template
- replace annotations with actual data for each employee
- save the file to be printed in the format LASTNAME_FIRSTNAME_document.txt in a directory called "generated"

# Guidelines

## CSV reading
CSV files are read via the csv module which is provided by Python. An example is here:
```
import csv

f = open('cities.csv')
reader = csv.reader(f)
for row in reader:
    column1 = row[0]
    column2 = row[1]
    print("{0} has {1} people".format(column1, column2))
f.close()
```
Of course other examples can be taken from the official documentation if they are clearer/simpler: https://docs.python.org/3/library/csv.html

## Template file
Consider this template. Create a file with these contents and read it, as previously shown in a string.
```
@@FIRST_NAME@@ @@LAST_NAME@@, born in @@ORIGIN@@, on @@BIRTH_DATE@@ you are required to sign this document in order to have access to company's new web portal. This is required by the company providing the new web portal.


@@NAME@@                                     @@TODAY_DATE@@
```

All the annotations, except @@TODAY_DATE@@ are taken from a csv file. @@TODAY_DATE@@ is the date of the document generation and can be obtained via the methods exposed by the datetime module (self study required in order to obtain the date: https://docs.python.org/3/library/datetime.html )

### Replacing the annotations
Replacing can be done via the "replace" function. Look at the following example:
```
>>> template="Hi, my name is, what? My name is, who? / My name is, chka-chka, @@NAME@@"
>>> template.replace("@@NAME@@","Slim Shady")
'Hi, my name is, what? My name is, who? / My name is, chka-chka, Slim Shady'
>>>
```

## Writing the file

This is already covered and nothing new is presented here.

## Creating a directory
This can be done via functions from os module. Self study is required: https://docs.python.org/3/library/os.html

Please be sure that the filename of the newly created file also includes the directory name. For example for writing the file "John_Smith_document.txt" in the "generated" directory the name of the file will be "generated/John_Smith_document.txt"

# Possible improvements

Creating your own modules in orer to have your code more manageable rather than have everything in a single file. Please see this tutorial https://docs.python.org/3/tutorial/modules.html
