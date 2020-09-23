# INPUT
"""
SYNTAX
input(Question)
"""

Name = input("Whats your Name? ")
print("Name:", Name)

# -------------------------------------------------
# File IO

# open(FileName, "r+") - Open File
"""
r - read
w - write
a - append
r+ - read and write
"""
# close() - Close File


# FileName.close() - Close File

# FileName.read() - Read File

# FileName.write("Something") - Write in a file

# FileName.readline() - There is a pointer that will read the file from the beginning
# If we read the line again, the pointer will move to the next element


# with Statement
# with open(FileName, "r") as FileVariable:
#   for line in FileName:
#     print(line)
