"""
  PYTHON IS EASY
  HomeWork Assignment 4
  STUDENT : Huzaifa Pitolwala
"""

myUniqueList = []
myLeftovers = []

def addToList(Anything):
  if Anything in myUniqueList:
    leftOvers(Anything)
  else:
    myUniqueList.append(Anything)

def leftOvers(Rejected):
  myLeftovers.append(Rejected)

addToList("1")
addToList("1")
addToList("2")

print("myUniqueList")
print(myUniqueList)
print("myLeftovers")
print(myLeftovers)
