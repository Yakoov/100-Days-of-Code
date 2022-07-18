# This exercise is to generate randomly a "Head" or "Tail"

import random

random_generator = random.randint(0,1)
if random_generator == 0:
    print("Heads")
else:
    print("Tails")
