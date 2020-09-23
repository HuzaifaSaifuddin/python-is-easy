"""
  PYTHON IS EASY
  HomeWork Assignment 2
  STUDENT : Huzaifa Pitolwala
"""

# Song Name
SongName = "Yahin Hoon Main"  # string

# Song Name Translation (Not exactly accurate)
Translation = "I am always here"

# Name of Artist
def ArtistName():
  return "Ayushmann Khurrana"

# Genre
def Genre():
  return "Romance"

# Duration
Duration = 300  # number

# Release Details
def IsReleased():
 return True

def ReleaseYear():
 return 2015

# Output
print("Name: " + SongName)

print("Translation: " + Translation)

print("Artist: " + ArtistName())

print("Genre: " + Genre())

print("Duration: " + str(Duration))

print("Released: " + str(IsReleased()))

print("Released in " + str(ReleaseYear()))

""" 
  OUTPUT
  -------
  Name: Yahin Hoon Main
  Translation: I am always here
  Artist: Ayushmann Khurrana
  Genre: Romance
  Duration: 300
  Released in 2015
"""
