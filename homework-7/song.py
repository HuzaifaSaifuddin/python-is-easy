"""
  PYTHON IS EASY
  HomeWork Assignment 7
  STUDENT : Huzaifa Pitolwala
"""

# Song Details
songDetails = { "Name": "Yahin Hoon Main", "Translation": "I am always here", "Artist": "Ayushmann Khurrana", "Genre": "Romance", "Duration": 300, "Release Year": 2015
              }

for key, value in songDetails.items():
  print(key + ": " + str(value))


def guessDetails(key, value):
  if key in songDetails:
    print(str(songDetails[key]) == value)
  else:
    print(False)

def guessSongInputs():
  userInputKey = input("Key : ")
  userInputValue = input("Value : ")
  guessDetails(userInputKey, userInputValue)

guessSongInputs()