#!/usr/bin/env python

# This code is under BSD 2-clause license

class Fish(object):
    """Constructor
        It receives the name of the fish
    """
    def __init__(self,name):
        self.name = name

    def GetFamily(self):
        return ""

    def ShowInfo(self):
        print '"' + self.name + "\" fish is from '" + self.GetFamily() + "' family"

class Salmon(Fish):
    def __init__(self):
        super(Salmon,self).__init__("Salmon")

    def GetFamily(self):
        return 'Salmonidae'

class WaleShark(Fish):
    def __init__(self):
        super(WaleShark, self).__init__("Wale shark")

    def GetFamily(self):
        return "Rhincodontidae"

class Pangasius(Fish):
    def __init__(self):
        super(Pangasius, self).__init__("Pangasius")

    def GetFamily(self):
        return "Pangasiidae"

fish1 = Salmon()
fish2 = Pangasius()

fishList = [ fish1 , fish2, WaleShark() ]

for fish in fishList:
    fish.ShowInfo()
