def gameBoard(rows, columns):
  for row in range(rows):
    if row%2 == 0:
      for column in range(1, columns):
        if column%2 == 1:
          if column != 5:
            print(" ", end = "")
          else:
            print(" ")
        else:
          print("|", end = "")
    else:
      print("-----")

gameBoard(5, 6)