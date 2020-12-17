# IMPORTING
"""
SYNTAX:
import LibraryName
"""
# NOTES
# import random
# random.randint(0,10) -> Gives a random integer within the given range.
# random.random()      -> Gives a random float value between 0 & 1.
# random.uniform(1,11) -> Gives a random float value within the given range.

# import time
# time.clock()  -> Gives current time.
# time.sleep(3) -> Pauese code for the given amount of time.

# import math         -> Example argument -> 3.14
# math.sqrt(Val)      -> Gives squareroot of a given argument (Output: 1.772004514666935)
# math.exp(Val)       -> Gives exponential value of a given argument (Output: 23.103866858722185)
# math.factorial(Val) -> Gives a factorial value of the given argument.Should be an Integer. (Output: 6)
# math.sin(Val)       -> Gives Sin value of the given argument (Output: 0.0015926529164868282)
# math.floor(Val)     -> Gives floor value of the given argument (Output: 3)
# math.ceil(Val)      -> Gives Ceiling value of the given argument (Output: 4)

# Importing the library 'random' as 'r' where 'r' is its nickname
import random as r

randInt = r.randint(0,10)
print(randInt)

# Alternative Import Method
# from random import *

#### Time Library
import time

currentTime = time.clock()

# sleep the processor for 3 seconds using 'sleep' function
time.sleep(3)

pastTime = time.clock()

print(pastTime - currentTime)

#### Math Library

import math

# square root of the variable 'Val' using 'sqrt' function
Val = 3.14
sqrtVal = math.sqrt(Val)
print(sqrtVal)
