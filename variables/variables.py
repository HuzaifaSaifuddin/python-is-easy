# VARIABLES

# Assigning Variables
one = 1
onePointOne = 1.1
strng = "String"

print(one)
print(onePointOne)
print(strng)

"""
1
1.1
String
"""

# Shorthand way of declaration variables
one, two, three = 1, 2, 3
print(one)
print(two)
print(three)
"""
1
2
3
"""

# String concatinated with integer will throw TypeError.
strng + one
# TypeError: cannot concatenate 'str' and 'int' objects
