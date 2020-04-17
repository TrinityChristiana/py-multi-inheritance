from flowers import Pesticides, PlantDescription

class Lily(Pesticides, PlantDescription):
    def __init__(self):
        super().__init__()
        self.name = "lily"
        self.description = "Lily, the common name applied to herbaceous flowering plants belonging to the genus Lilium of the family Liliaceae. The genus contains between 80 and 100 species, native to the temperate areas of the Northern Hemisphere. Lilies are prized as ornamental plants, and they have been extensively hybridized."