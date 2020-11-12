
# AirTour.py
from gd import *


class TripMeta:
    def __init__(self):
        self.m = None

class Trip:
    def __init__(self, loc = None, date = None, members = None,guide = None):
        self.Location = None
        self.date = None
        self.guide = guide
        self.party = members
        self.meta = TripMeta()


class Human(object):
    def __init__(self):
        self.name = None
        self.id = None
        self.contactInfo = None
        self.about = None
        self.photo = None
        self.birth = None


class Traveler(Human):
    def __init__(self):
        self.x = None

class Guide(Human):
    def __init__(self, cap = "Sneplin",avail = "Anytime"):
        self.capabilities = cap
        self.availability = avail
        self.area = "all"

##

def newHuman(name):
    print("New Human:",name)
    h = Human()
    h.name = name
    xo.humans[name] = h
    return h


def newGuide(name):
    print("New Guid:",name)
    g = Guide()
    g.name = name
    xo.guides[name] = g
    return g

h = newHuman("Omer")

g = newGuide("Meir")


def NewTrip():
    trip = Trip()
    print("where?")
    trip.Location = input()
    print("when?")
    trip.date = input()
    print("\n\n Cool! searching...\n")



    return trip

t = NewTrip()


print("_________________")
print(xo.guides.show())
print("_________________")
print(xo.humans.show())
