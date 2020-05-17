#!/usr/bin/env python

import gettext
import random
import sys

def tr(text):
    return gettext.gettext(text)

def pl(text, textpl,count):
    return gettext.ngettext(text,textpl,count)

class Animal:
    def __init__(self,name, name_plural,number_of_legs):
        self.name = name
        self.name_plural = name_plural
        self.number_of_legs = number_of_legs

    def __str__(self):
        return self.name

def get_animals():
    animals = []

    hen = Animal(tr("hen"),tr("hens"),2)
    animals.append(hen)

    rooster = Animal(tr("rooster"),tr("roosters"),2)
    animals.append(rooster)

    turkey = Animal(tr("turkey"),tr("turkeys"),2)
    animals.append(turkey)

    duck = Animal(tr("duck"),tr("ducks"),2)
    animals.append(duck)

    goose = Animal(tr("goose"),tr("geese"),2)
    animals.append(goose)

    ostrich = Animal(tr("ostrich"),tr("ostriches"),2)
    animals.append(ostrich)

    cat = Animal(tr("cat"),tr("cats"),4)
    animals.append(cat)

    pig = Animal(tr("pig"),tr("pigs"),4)
    animals.append(pig)

    dog = Animal(tr("dog"),tr("dogs"),4)
    animals.append(dog)
    
    sheep = Animal(tr("sheep"),tr("sheep"),4)
    animals.append(sheep)

    cow = Animal(tr("cow"),tr("cows"),4)
    animals.append(cow)

    lion = Animal(tr("lion"),tr("lions"),4)
    animals.append(lion)

    jaguar = Animal(tr("jaguar"),tr("jaguars"),4)
    animals.append(jaguar)

    return animals

def main():
    animals = get_animals()
    # split animals into groups depending on their legs
    two_legged = []
    four_legged = []

    for animal in animals:
        legs = animal.number_of_legs
        if legs == 2:
            two_legged.append(animal)
        elif legs == 4:
            four_legged.append(animal)

    #print ("2 legs:")
    #for animal in two_legged:
    #    print(animal)

    #print ("4 legs:")
    #for animal in four_legged:
    #    print(animal)

    two_legged_animal = two_legged[ random.randint(0,len(two_legged)-1) ]
    four_legged_animal = four_legged[ random.randint(0,len(four_legged)-1) ]

    how_many_two_legged = random.randint(0,20)
    how_many_four_legged = random.randint(0,20)

    total_heads = how_many_two_legged + how_many_four_legged
    total_legs = 2*how_many_two_legged + 4*how_many_four_legged

    heads = pl("%d head","%d heads",total_heads) % (total_heads)
    legs = pl("%d leg","%d legs",total_legs) % (total_legs)
    print("******************")
    print("******************")
    print(tr("In a backyard there are %s and %s.") % (two_legged_animal.name_plural,four_legged_animal.name_plural))
    print(tr("You have %s and %s") % (heads, legs))
    print(tr("How many %s?") % (two_legged_animal.name_plural))
    answer = sys.stdin.readline().strip()

    if int(answer) == how_many_two_legged:
        print(tr("Well done!"))
    else:
        print(tr("Wrong! There are:"))

    two_plural_form = pl(two_legged_animal.name,two_legged_animal.name_plural,how_many_two_legged)
    two_legged_str = tr("%d %s") % (how_many_two_legged,two_plural_form)
    print(two_legged_str)

    four_plural_form = pl(four_legged_animal.name,four_legged_animal.name_plural,how_many_four_legged)
    four_legged_str = tr("%d %s") % (how_many_four_legged,four_plural_form)
    print(four_legged_str)

if __name__=="__main__":
    main()
