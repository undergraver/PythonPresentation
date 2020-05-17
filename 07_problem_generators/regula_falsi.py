#!/usr/bin/env python

import gettext

def tr(text):
    # TODO implement translation
    return text

class Animal:
    def __init__(self,name, name_plural,number_of_feet):
        self.name = name
        self.name_plural = name_plural
        self.number_of_feet = number_of_feet


def get_animals():
    animals = []

    hen = Animal(tr("hen"),tr("hens"),2)
    animals.add(hen)

    rooster = Animal(tr("rooster"),tr("roosters"),2)
    animals.add(rooster)

    turkey = Animal(tr("turkey"),tr("turkeys"),2)
    animals.add(turkey)
    
    duck = Animal(tr("duck"),tr("ducks"),2)
    animals.add(duck)

    cat = Animal(tr("cat"),tr("cats"),4)
    animals.add(cat)

    pig = Animal(tr("pig"),tr("pigs"),4)
    animals.add(pig)

    dog = Animal(tr("dog"),tr("dogs"),4)
    animals.add(dog)
    
    sheep = Animal(tr("sheep"),tr("sheep"),4)
    animals.append(sheep)

    cow = Animal(tr("cow"),tr("cows"),4)
    animals.append(cow)

    return animals
