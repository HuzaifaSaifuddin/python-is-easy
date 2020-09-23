import sys
from termcolor import colored, cprint

def gameBoard():
  return [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

def availableSlots():
  return ['1', '2', '3', '4', '5', '6', '7']

def play():
  Board = gameBoard()

  print(availableSlots())
  printBoard(Board)

  StartGame(Board, StartChip())

def StartGame(Board, Chip, Count = 0):
  Slot = input("Select Slot (1-7): ")
  if Slot in availableSlots():
    Count += 1
    FillSlot(Board, int(Slot), Chip, 5, Count)
  elif Slot == "quit":
    exit()
  else:
    print('Invalid Input')
    StartGame(Board, Chip, Count)

def FillSlot(Board, IntSlot, Chip, AvailableSlot, Count):
  if Board[0][IntSlot - 1] != ' ':
    print('Slot Full Choose Different Slot')
    StartGame(Board, Chip, Count)
  elif Board[AvailableSlot][IntSlot - 1] == ' ':
    Board[AvailableSlot][IntSlot - 1] = Chip

    print(availableSlots())
    printBoard(Board)

    if CheckWinner(Board, Chip):
      print('-----------------------------')
      cprint(Chip + ' Won', 'green')
      print('Starting a new Game')
      print('-----------------------------')
      play()
    else:
      StartGame(Board, SwitchChip(Chip), Count)
  else:
    FillSlot(Board, IntSlot, Chip, AvailableSlot - 1, Count)
    
def StartChip():
  SelectedChip = input("Select Start Chip (X or O, default X): ")
  if SelectedChip == 'O':
    print('O Starts')
    return 'O'
  else:
    print('X Starts')
    return 'X'

def SwitchChip(Chip):
  if Chip == 'O':
    return 'X'
  else:
    return 'O'

def printBoard(Board):
  for row in Board:
    print(row)

def CheckWinner(Board, Chip):
  Row = 6
  Column = 7

  for x in range(Row):
    for y in range(Column):
      if x <= Row - 3 and Board[x][y] == Chip and Board[x + 1][y] == Chip and Board[x + 2][y] == Chip and Board[x + 3][y] == Chip:
        return True
      elif y <= Column - 3 and Board[x][y] == Chip and Board[x][y + 1] == Chip and Board[x][y + 2] == Chip and Board[x][y + 3] == Chip:
        return True
      elif x <= Row - 3 and y <= Column - 3 and Board[x][y] == Chip and Board[x + 1][y + 1] == Chip and Board[x + 2][y + 2] == Chip and Board[x + 3][y + 3] == Chip:
        return True
      elif x >= 3 and y <= Column - 4 and Board[x][y] == Chip and Board[x - 1][y + 1] == Chip and Board[x - 2][y + 2] == Chip and Board[x - 3][y + 3] == Chip:
        print([x, y])
        return True

  return False

play()
