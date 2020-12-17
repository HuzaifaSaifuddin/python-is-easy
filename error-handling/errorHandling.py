# Exceptions

# Syntax
# try:      -> Try to run code
#   code
# except:   -> Raises exception and prints the code.
#   pass
#   code
# finally:  -> Do Something at the end.
#   code

# raise Error -> Manually raise error

try:
  # Printing 'Hello' using the 'print()' function
  print(int("Hello"))
except:
  # Printing 'Enterted Exception' only if any errors occur in the try block using the 'print()' function
  pass # -> To pass the exception if we dont want to print/return anything
  print("Entered exception")


keyword="Hello"
try:
    # Printing variable 'keyword' using the 'print()' function
    print(int(keyword))
except Exception as e:
    # Printing the string version of the catched exception,
    # The exception that has occured can be caught and stored in a variable
    print(str(e))


try:
    # Printing variable 'keyword' using the 'print()' function
    print(int(keyword))
# If known a specific error can be caught using the 'except' keyword
except ValueError:
    # Pinting "got a ValueError" using 'print()' function
    print("got a ValueError")


try:
  # Printing variable 'keyword' using the 'print()' function
  raise NameError
# If known a specific error can be caught using the 'except' keyword
except ValueError:
  # Printing "got a ValueError" using 'print()' function
  print("got a ValueError")
# except can be chained together like if elif statements
except:
  # Printing "Other types of exception" using 'print()' function
  print("Other types of exception")
# The 'finally' block is a block always executed , no matter what happens in the 'try' 'except' block
finally:
  # Printing "finally" using 'print()' function
  print("finally")
