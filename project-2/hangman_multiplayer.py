import random
import getpass

# This function randomly pulls a word out of my word bank random_wordbank and names it secret_word
def get_secret_word():
  random_wordbank = ["lemon","orange","grapefruit","apple","lychee","pear","banana","melon","watermelon","honey"] # word bank of potential secret words
  pick_word = random.randint(0, len(random_wordbank)-1) # choose a random integer in range of wordbank length to use as the secret word
  return random_wordbank[pick_word]

# Guessing letters function
def letter_picking(secret, blank_word, num_lives):
  guessed_letter = input("Please guess a letter.") # user guesses a letter here
  lives_flag = 0 # set counter to 0 to begin recording number of correct guesses
  for i in [i for i,x in enumerate(secret) if x == guessed_letter]: # if x is the guessed letter, replace blank space with x
    lives_flag = 1 # guess is correct, so we add one to the counter
    blank_word[i] = guessed_letter
  num_lives = validate_lives(lives_flag, num_lives) # call new function to compute number of lives after completed loop
  print(num_lives)
  return blank_word, num_lives

# This function counts the number of lives needed to calculate the score and end the game
def validate_lives(lives_flag, lives):
  if lives_flag > 0: # check if counter value > 0, if it is, user guessed correctly
    print("Num lives unchanged",len(lives))
    print(lives)
    return lives
  else:
    lives.append("1") # if counter value not >0, then user guessed incorrectly. add "1" to num_lives as counter for lost lives
    print("You lost a life",len(lives))
    print(lives)
    return lives

def check_win(lives, blank, player_num, game_status):
  print(("check_win" ,blank))
  count_space = 0
  for i in range(len(blank)):
    if blank[i] is "_":
      pass
    else:
      count_space += 1
  if count_space == len(blank):
    print("You win")
    print("player number: ",player_num)
    game_status = True
    return game_status
  else:
    game_status = False
    return game_status
    
def single_player():
  num_lives = []  # array for single player lives
  return num_lives

def multi_player():
  num_lives = []  # array for two player lives for player 1
  num_lives2 = [] # array for two player lives for player 2   


def main():
  num_players = input("Please enter, '1' if you would like to play in single player mode or, '2' if you would like to play in two player mode.")
  if num_players == '1':
    game_over = False
    # num_lives = single_player()
    num_lives = []
    print(len(num_lives))
    player = 1
    secret_word = get_secret_word()            # Stabilize a random word to guess
    # print(secret_word)
    blanks = list(secret_word)                 # Create list containing each letter of secret_word separated by ","
    # print(blanks)
    for i in range(len(blanks)):               # Re-write each item in "blanks = list(secret_word)" to "_" for game play
      blanks[i] = "_"
    print(blanks)
    # print(("lives_flag at start =", lives_flag))
    print(len(num_lives))
    while len(num_lives) < 3 and game_over == False: # Set game play to end after 3 incorrect guesses, i.e. 0 lives left
      blanks, num_lives = letter_picking(secret_word, blanks, num_lives)
      game_over = check_win(num_lives, blanks, player, game_over)
    print(num_lives)
    print(game_over)
    thingy = True
    print(thingy)
    print("Game Over. Do you want to play again?" )
    num_lives[:] = []
    # del game_over
    play_again = input("Enter character 'y' or 'n' ")
    while not play_again is 'y' or play_again is 'n':
      if len(play_again) != 1:
        print("Only one character please")
      elif play_again is not 'y' and play_again is not 'n':
        print("Only a 'y' or 'n' please")
      elif play_again is 'y':
        # write code to play the game again
        pass
      else:
        print("Thank you for playing")
        break
  elif num_players == '2':
    # word1 = input("Player 1: Please enter a word for your opponent to guess.")
    word1 = getpass.getpass("Player 1: Please enter a word for your opponent to guess.")
    # word2 = input("Player 2: Please enter a word for your opponent to guess.")
    word2 = getpass.getpass("Player 2: Please enter a word for your opponent to guess.")
    blanks1 = list(word1)
    blanks2 = list(word2)
    num_lives = []  # array for two player lives for player 1
    num_lives2 = [] # array for two player lives for player 2
    game_over = False
    # print(blanks1)
    for i in range(len(blanks1)):
      blanks1[i] = "_"
    print("Player 2: You are guessing the following:", blanks1)
    # print(blanks2)
    for i in range(len(blanks2)):
      blanks2[i] = "_"
    print("Player 1: You are guessing the following:",blanks2)
    while len(num_lives) < 3 and len(num_lives2) < 3 and game_over == False:
      player = 1
      blanks, num_lives = letter_picking(word1, blanks1, num_lives)
      game_over = check_win(num_lives, blanks1, player, game_over)
      player = 2
      blanks, num_lives2 = letter_picking(word2, blanks2, num_lives2)
      game_over = check_win(num_lives2, blanks2, player, game_over)
    if num_lives > num_lives2:
      print("Player 2 wins")
    elif num_lives < num_lives2: 
      print("Player 1 wins")
    else:
      print("Tie")
    print(blanks1)
    print(blanks2)
  else:
    print("User Response Error: Please enter, '1' or, '2'.")
    
if __name__ == "__main__":
  main()
