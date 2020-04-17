from animals.movements import IDigging, ISlither
from animals.animal import Animal

class Earthworm(Animal, IDigging, ISlither):
    def __init__(self, name):
        Animal.__init__(self, "earthworm")
        self.name = name