from animals.movements import IFly, IHopping
from animals.animal import Animal

class Finch(Animal, IFly, IHopping):
    def __init__(self, name):
        Animal.__init__(self, "finch")
        self.name = name