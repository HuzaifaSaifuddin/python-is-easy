# IF STATEMENTS
"""
SYNTAX:
if condition:
  Action
elif condition:
  Action
else condition:
  Action
"""

click = True
Like = 0

if click == True:
  Like = Like + 1
  click = False

print(Like)
# Output
# 1

# Another Example
Time = "Night"
Sleepy = False
Pajamas = "Off"

if Time == "Night" or Sleepy == True:
  Pajamas = "On"
print(Pajamas)

# Output
# "On"


# elif Example

Time = 'Day'

if Time == "Night":
  Pajamas = "On"
elif Time == "Day":
  Pajamas = "Off"
else:
  Pajamas = "Off"

print(Pajamas)
# Output
# Off
