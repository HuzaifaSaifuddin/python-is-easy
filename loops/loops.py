# LOOPS

# ------------------------------------------------------------------------------------------------

# For Loops
print("***For Loops***")
"""
SYNTAX:
for s in String:
  print(s)
"""

Word = "Hello" #String

for w in Word:
  print(w)

# Output
# H
# e
# l
# l
# 0

# Integer is not iterable

Numbers = [1, 2, 3, 4, 5] #Array
for l in Numbers:
  print(l)

# Output
# 1
# 2
# 3
# 4
# 5

# Range Function - range(start, stopping, steps) - "stopping", "steps" are optional
Numbers = []
for num in range(1, 10, 2):
  Numbers.append(num)

print(Numbers)

# Output
# [1, 3, 5, 7, 9]

# ------------------------------------------------------------------------------------------------

# While Loops
print("***While Loops***")
"""
SYNTAX:
while condition:
  Action1
  Action2
"""

counter = 1

while (counter <= 5):
  print(counter)
  counter = counter + 1

# Output
# 1
# 2
# 3
# 4
# 5

# ------------------------------------------------------------------------------------------------

# Breaking & Continuing Loops
print("***Breaking & Continuing Loops***")
"""
break - in a loop will break a loop
continue - in a loop will continue if condition matches
"""

Participants = ["Jen", "Alex", "Tina", "Joe", "Ben"]
position = 0

for name in Participants:
  if name == "Tina":
    break
  position = position + 1

print(position)
# 2

for number in range(5):
  if number%3 == 0:
    print(number)
    print("Divisible by 3")
    continue
  print(number)
  print("Not Divisible by 3")

# 0
# Divisible by 3
# 1
# Not Divisible by 3
# 2
# Not Divisible by 3
# 3
# Divisible by 3
# 4
# Not Divisible by 3
