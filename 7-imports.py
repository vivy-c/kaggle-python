# python3 /Users/vivycahyani/Desktop/Belajar/kaggle-python/7-imports.py

import math

print("It's math! It has type {}".format(type(math)))
print(dir(math))
print("pi to 4 significant digits = {:.4}".format(math.pi))
math.log(32, 2)
print(math.log(32, 2))
help(math.log)
print(help(math.log))
print(help(math))
import math as mt
print(mt.pi)
mt = math

from math import *
print(pi, log(32, 2))

from math import *
from numpy import *
print(pi, log(32, 2))