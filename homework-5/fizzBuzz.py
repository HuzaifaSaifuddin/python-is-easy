"""
  PYTHON IS EASY
  HomeWork Assignment 5
  STUDENT : Huzaifa Pitolwala
"""


def fizzBuzz(Number):
  for num in range(Number):
    num += 1
    Output = ""

    # Check for Prime
    for x in range(num):
      if num == 1:                    # 1 is Not Prime
        Output = "Not Prime"
      elif x >= 2 and x != num:         # num should not be divisible by any no. other that 1 or self
        if (num % x == 0):            # if num is divisible by no. < itself, num is not Prime
          Output = "Not Prime"
          break
        else:                         # if num is not divisible by no. < itself, num is Prime
          Output = "Prime"
      else:
        Output = "Prime"              # 2 will drop in else condition and it is always a prime

    # FizzBuzz
    if (num % 3 == 0) and (num % 5 == 0):            # if num is divisible by 3 & 5, print FizzBuzz
      print(str(num) + " -> FizzBuzz | " + Output)
    elif (num % 3 == 0):                             # if num is divisible by 3, print Fizz
      print(str(num) + " -> Fizz | " + Output)
    elif (num % 5 == 0):                             # if num is divisible by 3, print Buzz
      print(str(num) + " -> Buzz | " + Output)
    else:
      print(str(num) + " -> " + Output)


# Enter anyNumber in fizzBuzz Function
fizzBuzz(100)
