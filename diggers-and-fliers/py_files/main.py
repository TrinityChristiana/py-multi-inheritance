# **************************** Challenge: Diggers and Fliers ****************************
 
'''
Author: Trinity Terry
pyrun: python main.py
'''
from animals import Earthworm, Terrapin, TimperRattlesnake, Mouse, Ant, Finch, BettaFish, CopperheadSnake, Gerbil, Parakeet
from temp_containers import IAir, ILand, IUnderground, IWater
"""
Animals
    Ants - Dig, walk
    Earthworms - Dig, slither

    Terrapins - Dig, swim, walk
    Betta Fish - swim
"""

earthworm = Earthworm("earthy")
worm = Earthworm("yeah")
terrapin = Terrapin("terror")
timper = TimperRattlesnake("temper")
mouse = Mouse("mousey")
ant = Ant("antsy")
finch  = Finch("atticus")
betta = BettaFish("alpha")
copper = CopperheadSnake("tooper")
gerbil = Gerbil("germy")
keet = Parakeet("keet")

cage = IAir("Circus")
land_terrarium = ILand("Sahera")
under_terrarium = IUnderground("Earth")
aquarium = IWater("Sea World")

aquarium.add_animal(terrapin, betta)
under_terrarium.add_animal(ant, earthworm, worm)
land_terrarium.add_animal(gerbil, copper, mouse, timper)
cage.add_animal(finch, keet)

print(cage, land_terrarium, under_terrarium, aquarium) 
