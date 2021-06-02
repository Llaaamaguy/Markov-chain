import os
from .generate import generate

class UI:
  def ui():
    while True:
      usrinput = input("markov_chain_project: ")
      usrwords = usrinput.split()
      if usrwords[0] == "help":
        print('START    Starts the training process \n [type]                  [file]\ntype in custom text     get text from a file\n\nREDO     Redo the last command\n\nEXIT     Exits the program')
      elif usrwords[0] == "start":
        with open("lastcommand.txt", "a") as f:
          f.write("start ")
        if usrwords[1] == "type":
          with open("lastcommand.txt", "a") as f:
            f.write("type\n")
          print('\n')
          print(generate.gencustom())
        elif usrwords[1] == "file":
          with open("lastcommand.txt", "a") as f:
            f.write("file ")
          print('\n')
          print(generate.genfile("nondefined"))
      elif usrwords[0] == "redo":
        with open('lastcommand.txt', 'rb') as f:
          f.seek(-2, os.SEEK_END)
          while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
          command = f.readline().decode()
        command = command.split()
        print('\n')
        if command[0] == "start":
          if command[1] == "type":
            print(generate.gencustom())
          elif command[1] == "file":
            fname = command[2]
            length = command[3]
            length = int(length)
            print(generate.genfile("predefined", fname, length))
      elif usrwords[0] == "exit":
        break
      else:
        print("Unknown command: " + usrwords[0])