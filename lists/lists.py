# LISTS

Scores = [70, 85, 67.5, 90, 80]
print(Scores)
# [70, 85, 67.5, 90, 80]

print(Scores[0])
print(Scores[1])
print(Scores[2])
print(Scores[3])
print(Scores[4])
# 70
# 85
# 67.5
# 90
# 80

print(Scores[0:2])
# [70, 85]

print(Scores[2:])
# [67.5, 90, 80]

# Modifying List
Scores[0] = 65
print(Scores)
# [65, 85, 67.5, 90, 80]

# Append Element
Scores.append(82)
print(Scores)
# [65, 85, 67.5, 90, 80, 82]


print(Scores[6])
# IndexError: list index out of range
