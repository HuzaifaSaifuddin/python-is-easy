# SETS

Sets = { "Element1", "Element2", "Element1", "Element4" }
print(Sets)
print(len(Sets))

# s={1, 2, 3, [4, 5]}
# print(s)
# TypeError: unhashable type: 'list'


# DICTIONARIES

Dictionary = { "Key": "value", "Key1": { "newKey": "newValue" }, "Key2": ["ValueA", "Value2"] }
print(Dictionary)
print(len(Dictionary))

print("PRINT KEYS & VALUES BOTH.")
for key, value in Dictionary.items():
  print(key + ": " + str(value))

print("PRINT KEYS.")
for keys in Dictionary:
  print(keys)

print("PRINT KEYS DECLARING keys().")
for keys in Dictionary.keys():
  print(keys)

print("PRINT VALUES.")
for value in Dictionary.values():
  print(value)

# OUTPUT
# {'Key': 'value', 'Key1': {'newKey': 'newValue'}, 'Key2': ['ValueA', 'Value2']}
# 3
# PRINT KEYS & VALUES BOTH.
# Key: value
# Key1: {'newKey': 'newValue'}
# Key2: ['ValueA', 'Value2']
# PRINT KEYS.
# Key
# Key1
# Key2
# PRINT KEYS DECLARING keys().
# Key
# Key1
# Key2
# PRINT VALUES.
# value
# {'newKey': 'newValue'}
# ['ValueA', 'Value2']
