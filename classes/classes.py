# CLASSES
"""
SYNTAX:
class ClassName:
  def __init__(self):
    self.Name = "Huzaifa "
"""

class Team:
  def __init__(self, Name, Origin):
    self.TeamName = Name
    self.TeamOrigin = Origin

  def DefineTeamName(self, Name):
    self.TeamName = Name

  def DefineTeamOrigin(self, Origin):
    self.TeamOrigin = Origin

Team1 = Team("Name", "Origin")

# Method to replace Name
Team1.DefineTeamName("Tigers")
print(Team1.TeamName)

# Method to replace Origin
Team1.DefineTeamOrigin("Chicago")
print(Team1.TeamOrigin)

# Arguments directly from Initialize
Team2 = Team("Cheetah", "India")

print(Team2.TeamName)
print(Team2.TeamOrigin)


# ClassInheritance

# class InheritanceClassName(ParentClass):
#   def __init__(self, Input1, Input2):
#     ParentClass.__init__(self)
#     self.Attribute1 = Input1
#     self.Attribute2 = Input2
#     self.Attribute3 = 0

#   def AnotherMethod(self):
#     Action(s)
print("Inheritance")

class Player(Team):
  def __init__(self, PlayerName, PPoints, TeamName, TeamOrigin):
    Team.__init__(self, TeamName, TeamOrigin)
    self.PlayerName = PlayerName
    self.PlayerPoints = PPoints

  def ScoredPoint(self):
    self.PlayerPoints += 1

  def setName(self, name):
    self.PlayerName = name

  def __str__(self):
    return self.PlayerName + " has scored: " + str(self.PlayerPoints) + " Points"

Player1 = Player("Sid", 0, "Sharks", "Chicago")
print(Player1.PlayerName)
print(Player1.PlayerPoints)
#Player1.DefineTeamName("Sharks")
print(Player1.TeamName)
print(Player1.TeamOrigin)
Player1.ScoredPoint()
print(Player1.PlayerPoints)
Player1.setName("Lee")
print(Player1.PlayerName)
print(Player1)
