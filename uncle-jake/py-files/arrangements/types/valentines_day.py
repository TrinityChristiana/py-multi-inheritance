from arrangements import Arrangement

class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()
        self.stem_inch = 7
        self.refrigerated = True
        self.descriptor  = "flamboyant"

    def enhance(self, *args):
        try:
            
            for i in args:
                if i.uses_pesticides:
                    self.flowers.append(i)
                else:
                    raise AttributeError("Only roses, lillies, and alstroemeria cal be addded to a ValentinesDay arrangement")
        except AttributeError as taco:
            print(f"AttributeError: Only roses, lillies, and alstroemeria can be addded to a Valentines Day arrangement")

