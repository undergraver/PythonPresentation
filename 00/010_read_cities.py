import csv

f = open('cities.csv')
reader = csv.reader(f)
for row in reader:
    column1 = row[0]
    column2 = row[1]
    print("{0} has {1} people".format(column1, column2))
f.close()
