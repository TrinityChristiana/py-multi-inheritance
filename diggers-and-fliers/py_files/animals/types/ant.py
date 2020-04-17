from animals.movements import IDigging, IWalking
from animals.animal import Animal

class Ant(Animal, IDigging, IWalking):
    def __init__(self, name):
        Animal.__init__(self, "ant")
        self.name = name