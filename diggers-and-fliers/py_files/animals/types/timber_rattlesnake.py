from animals.movements import ISlither, ISwimming
from animals.animal import Animal

class TimperRattlesnake(Animal, ISlither, ISwimming):
    def __init__(self, name):
        Animal.__init__(self, "timper rattlesnake")
        self.name = name