from temp_containers import Habitat

class ILand(Habitat):
    def __init__(self, name):
        super().__init__("land")
        self.name = name