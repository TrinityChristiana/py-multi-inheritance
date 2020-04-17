class Animal():
    def __init__(self, type_str):
        self.__type = type_str

    def __str__(self):
        motions = []
        poss = ["dig", "hop", "slither", "swim", "walk"]
        for i in poss:
            if i in dir(self): motions.append(f"{i}s")
            
        if "fly" in dir(self): motions.append("flies")

        return f"\n A {self.type} named {self.name.capitalize()} that {' and '.join([', '.join(motions[:-1]),motions[-1]] if len(motions) > 2 else motions)} \n \n"

    @property
    def type(self):
        return self.__type

    
