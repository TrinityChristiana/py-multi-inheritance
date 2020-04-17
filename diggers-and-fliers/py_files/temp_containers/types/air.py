from temp_containers import Habitat

class IAir(Habitat):
    def __init__(self, name):
        super().__init__("air")
        self.name = name