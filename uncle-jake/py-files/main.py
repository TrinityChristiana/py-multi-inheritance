# **************************** Challenge: Uncle Jakes Flower Shop ****************************

'''
Author: Trinity Terry
pyrun: python main.py
'''
from arrangements import MothersDay, ValentinesDay
from flowers import Rose, Lily, Alstroemeria, BabyBreath, Dasiy, Poppy
'''
Arrangements: Mothers, Valentines

Types: dasies, babybreath, poppies, rose, lilies, alstroemeria
    - stem size, refreidgeratrateed, 
    roses have clors pink, red, and blue

'''

#
if __name__ == "__main__":
    # Create Mothers Day Arrangement
    for_luna = MothersDay()
    # Create Valentines Day Arrangement
    for_beth = ValentinesDay()

    # create FLower Instances

    poppy = Poppy()
    daisy = Dasiy()
    baby_breath = BabyBreath()
    red_rose = Rose("red")
    pink_rose = Rose("pink")
    blue_rose = Rose("blue")
    lily = Lily()
    alstro_flower = Alstroemeria()
    print(poppy, daisy, baby_breath, red_rose, pink_rose, blue_rose, lily, alstro_flower)

    for_luna.enhance(daisy, poppy, baby_breath)

    for_beth.enhance(red_rose, blue_rose, pink_rose, lily, alstro_flower)

    print(for_beth)
    print(for_luna)

