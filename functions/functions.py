# FUNCTIONS
"""
SYNTAX:
def functionName(Input):
  Action
  return Output
"""

def addOne(Number):
  Output = Number + 1
  return Output

Var = 0
Var2 = addOne(Var)

print(Var2)

# With more than 1 Input
def addOneAddTwo(NumberOne, NumberTwo):
  Output = NumberOne + 1
  Output += NumberTwo + 2
  return Output

Sum = addOneAddTwo(1, 2)
print(Sum)
