from flowers import Pesticides, PlantDescription

class Alstroemeria(Pesticides, PlantDescription):
    def __init__(self):
        super().__init__()
        self.name = "alstroemeria"
        self.description = "Amaryllidaceae, amaryllis family of perennial herbs in the flowering plant order Asparagales, containing 73 genera and at least 1,600 species, distributed primarily in tropical and subtropical areas of the world. Members of the family have bulbs or underground stems, several strap- or lance-shaped leaves grouped at the base of the stem or arranged alternately along the stem, flowers usually with three or six petals and three or six sepals, and fruits that are typically dry capsules or fleshy berries."