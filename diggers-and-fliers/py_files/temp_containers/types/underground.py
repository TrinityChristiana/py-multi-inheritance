from temp_containers import Habitat

class IUnderground(Habitat):
    def __init__(self, name):
        super().__init__("underground")
        self.name = name