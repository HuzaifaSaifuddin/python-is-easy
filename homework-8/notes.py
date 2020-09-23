import os

FileName = input("Please provide filename : ")

def PlayFile(FileName, option):
  if option == "A":
    ReadFile = open(FileName, "r")  # Open File
    print(ReadFile.read()) # read File
    ReadFile.close() # Close it back

  elif option == "B":
    open(FileName, 'w').close() # Open and Close to empty File

  elif option == "C":
    Note = input("Add your Note?\n") # Input From User

    AppendFile = open(FileName, "a") # Open File using a(append)
    AppendFile.write(str(Note) + "\n") # Write in new Line
    AppendFile.close() # Close File

  elif option == "D":
    LineNumber = input("Line No. to be replaced? ")
    NewText = input("New Text ")

    # Code to Replace Line
    with open(FileName, 'r+') as file:
      # Read Lines
      lines = file.readlines()

      # Set Position
      position = int(LineNumber)

      # Insert a position 1 above
      lines.insert(position - 1, str(NewText) + "\n")

      # Remove existing Line at Position
      RemoveLine = lines[position]
      lines.remove(RemoveLine)

      # Open/Close file to empty it
      open(FileName, 'w').close()

      # Seek The cursor to bring on First Line
      file.seek(0)
      # Write each line in File again
      for i in lines:
        i.strip()
        file.write(str(i))
  else:
    print("Invalid Option")


while(True):
  if(os.path.exists(FileName)): # Check if File Exists
    print("A) Read the file")
    print("B) Delete the file and start over")
    print("C) Append the file")
    print("D) Replace a Line")
    print("E) Exit")

    userInput = input("Please choose A, B, C, D or E : ")

    if userInput == "E":
      break
    else:
      PlayFile(FileName, userInput)
  else:
    NewFile = open(FileName, "w") # Open with W, creates new file
    NewNote = input("Add your Note?\n")

    NewFile.write(str(NewNote) + "\n") # Write on File
    NewFile.close() # Close File

