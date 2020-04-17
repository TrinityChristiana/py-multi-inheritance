from temp_containers import Habitat

class IWater(Habitat):
    def __init__(self, name):
        super().__init__("water")
        self.name = name