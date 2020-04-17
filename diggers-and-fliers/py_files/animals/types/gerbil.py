from animals.movements import IDigging, IHopping
from animals.animal import Animal

class Gerbil(Animal, IDigging, IHopping):
    def __init__(self, name):
        Animal.__init__(self, "gerbil")
        self.name = name