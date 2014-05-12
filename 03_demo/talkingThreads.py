#!/usr/bin/env python

# This code is under BSD 2-clause license

from Queue import Queue
from threading import Thread
import time

class Actor(Thread):
    def __init__(self,name,lines):

        # this calls the Thread.__init__ method
        super(Actor, self).__init__(target=self)

        self.queue = Queue()
        self.name = name
        self.colleague = None
        self.lines = lines

    def run(self):
        counter = 0
        while counter < len(self.lines):

            self.WaitForMicrophone()

            print self.name + ":" + self.lines[counter]

            time.sleep(1)
            self.colleague.GiveMicrophone()

            counter = counter + 1

    def WaitForMicrophone(self):
        self.queue.get()

    def GiveMicrophone(self):
        self.queue.put(0)

JulianaLines = []
ProsperoLines = []

JulianaLines.append( "Prince Prospero, why do you roam the late night corridors?" )
ProsperoLines.append( "Sleep eludes me." )
JulianaLines.append("You have disturbing thoughts?")
ProsperoLines.append("And you Juliana what keeps you awake?")
JulianaLines.append("I think my thoughts dwell on the same subject as yours, the peasant girl.")
ProsperoLines.append("She has a perfect faith.")
JulianaLines.append("So do I, in you and in what you believe, I've been an eager student but I've held back from the final cerimonies, and now I'm ready to join you at the invocation.")
ProsperoLines.append("[laughing] How truly realistic women are, finally you are ready to dare the most terrible rites and incantations to secure your position here. I wonder if she is ready to dare as much if anything for the sake of love.")

##############

actorJuliana = Actor("Juliana",JulianaLines)
actorProspero = Actor("Prospero",ProsperoLines)

actorProspero.colleague = actorJuliana
actorJuliana.colleague = actorProspero

actorJuliana.start()
actorProspero.start()

actorJuliana.GiveMicrophone()
