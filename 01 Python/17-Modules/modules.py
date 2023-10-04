from math import pi
import math
from rps7 import rock_paper_scissors
import bulgaria
from enum import Enum
import random as rdm
import sys

# print everything in the Random module
for item in dir(rdm):
    print(item)

print(math.pi)  # 3.141592653589793
print(pi)  # 3.141592653589793


print(bulgaria.capital)  # Sofia
bulgaria.randomfunfact()

print("__name__", __name__)
print("bulgaria.__name__", bulgaria.__name__)  # bulgaria (not __main__)

# rock_paper_scissors()
print(rock_paper_scissors.__name__)  # play_rps (not __main__)

sys.exit("Bye!")
