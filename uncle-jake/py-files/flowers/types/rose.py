from flowers import Pesticides, PlantDescription

class Rose(Pesticides, PlantDescription):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.name = "rose"
        self.description = "Rose, (genus Rosa), genus of some 100 species of perennial shrubs in the rose family (Rosaceae). Roses are native primarily to the temperate regions of the Northern Hemisphere. Many roses are cultivated for their beautiful flowers, which range in colour from white through various tones of yellow and pink to dark crimson and maroon, and most have a delightful fragrance, which varies according to the variety and to climatic conditions."