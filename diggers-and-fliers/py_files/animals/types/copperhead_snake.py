from animals.movements import ISlither, ISwimming
from animals.animal import Animal

class CopperheadSnake(Animal, ISlither, ISwimming):
    def __init__(self, name):
        Animal.__init__(self, "copperhead snake")
        self.name = name