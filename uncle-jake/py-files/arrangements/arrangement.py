class Arrangement:
    def __init__(self):
        self.flowers = []
   
    def enhance(self, *args):
        self.flowers.extend([i for i in args])  

    def __str__(self):
        new_dict = self.__dict__
        flower_names = [i["name"] for i in [j.__dict__ for j in self.flowers]]
        combined_flowers = list(set(flower_names))
        flower_count = {i: flower_names.count(i) for i in combined_flowers}
        new_dict["flowers"] = flower_count
        string = f"This arrangement contains {', '.join([f'{v} {k}s' for k, v in new_dict['flowers'].items()])} which each have {new_dict['stem_inch']}-inch stems, {'need to be refrigerated' if new_dict['refrigerated'] else 'does not need to be refrigerated'}, and are {new_dict['descriptor']}"
        
        return string