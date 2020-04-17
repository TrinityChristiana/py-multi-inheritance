from animals.movements import IFly, IWalking, IHopping
from animals.animal import Animal

class Parakeet(Animal, IFly, IWalking, IHopping):
    def __init__(self, name):
        Animal.__init__(self, "parakeet")
        self.name = name