from animals.movements import ISwimming, IWalking, IHopping
from animals.animal import Animal

class Mouse(Animal, ISwimming, IWalking, IHopping):
    def __init__(self, name):
        Animal.__init__(self, "mouse")
        self.name = name