from animals.movements import IDigging, ISwimming, IWalking
from animals.animal import Animal

class Terrapin(Animal, IDigging, ISwimming, IWalking):
    def __init__(self, name):
        Animal.__init__(self, "terrapin")
        self.name = name