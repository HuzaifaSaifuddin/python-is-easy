"""
  PYTHON IS EASY
  HomeWork Assignment 3
  STUDENT : Huzaifa Pitolwala
"""

def checkEquality(NumberA, NumberB, NumberC):
  if ( int(NumberA) == int(NumberB)):
    return True
  elif (int(NumberB) == int(NumberC)):
    return True
  elif (int(NumberC) ==  int(NumberA)):
    return True
  else:
    return False

print("Is any 2 two of (1,2,2) Equal?")
print(checkEquality(1,2,2))

print("Is any 2 two of (1,2,3) Equal?")
print(checkEquality(1,2,3))

print("Is any 2 two of (1,2,'1') Equal?")
print(checkEquality(1,2,"1"))