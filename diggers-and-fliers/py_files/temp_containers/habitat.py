class Habitat:
    def __init__(self, type_str):
        self.animals = []
        self.__type = type_str

    @property
    def type(self):
        return self.__item

    def add_animal(self, *args):
        self.animals.extend([i for i in args])

    def __str__(self):
        animals = set([i.type for i in self.animals])
        animal_dict = dict()
        for animal in animals:
            animal_dict[f"{animal}"] = []
        for i in self.animals:
            animal_dict[f"{i.type}"].append(i.name.capitalize())
        first_draft = [f"{a.capitalize()}s ({' and '.join([', '.join(v[:-1]),v[-1]] if len(v) > 2 else v)})" for a in animals for k, v in animal_dict.items() if k == a]

        animal_display_str = ' and '.join([', '.join(first_draft[:-1]),first_draft[-1]] if len(first_draft) > 2 else first_draft)
        
        return f"\n This is a {self.__type} habitat called {self.name} with the following animals: {animal_display_str} \n \n"