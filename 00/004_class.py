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
    
    def IsCityLarge(self):
        ret = (self.population > 500000)
        return ret


p = City("Paris","France",11000000)
l = City("London","UK",9000000)
b = City("Brasov","RO",300000)

for city in [ p, l, b]:
    if city.IsCityLarge():
        print(f"{city.name} is large.")
    else:
        print(f"{city.name} is small.")

print(p)
print(l)

print(p+l)

print(p.name)
print(l.population)
print(l.country)
