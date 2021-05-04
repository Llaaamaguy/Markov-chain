from itertools import tee
import random
import os

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def generate_dict(userinput):
    words = userinput.split()
    worddict = {}
    for i, j in pairwise(words):
      if i in worddict:
        if j in worddict[i]:
          worddict[i][j] += 1
        else:
          worddict[i][j] = 1
      else:
        worddict[i] = {j: 1}
    return worddict

def generate_text(worddict, length):
  """
  generate text using tHe RiGhT wAy oF DoInG iT
  """

def generate_bad_text(worddict, length):
  string = []
  for i in range(length):
    if i == 0:
      string.append(random.choice(list(worddict.keys())))
    else:
      lastword = string[i-1]
      if lastword not in worddict:
        string.append(random.choice(list(worddict.keys())))
      else:
        choosablewords = []
        for k, v in worddict[lastword].items():
          for i in range(v):
            choosablewords.append(k)
        string.append(random.choice(choosablewords))
  return string

def gencustom():
  string = input("What is your training input: ")
  length = int(input("Length of output: "))
  worddict = generate_dict(string)
  generated = generate_bad_text(worddict, length)
  return(" ".join(generated))

def genfile(mode, fname=None, length=None):
  if mode == "nondefined":
    fname = input("File name: ")
    length = int(input("Length: "))
    with open("lastcommand.txt", "a") as f:
      f.write(fname + " " + str(length) + "\n")
  try:
    with open(fname, "r") as f:
      text = f.read()
    worddict = generate_dict(text)
    generated = generate_bad_text(worddict, length)
    return(" ".join(generated))
  except FileNotFoundError:
    return("File did not exist")

def main():
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
        print(gencustom())
      elif usrwords[1] == "file":
        with open("lastcommand.txt", "a") as f:
          f.write("file ")
        print('\n')
        print(genfile("nondefined"))
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
          print(gencustom())
        elif command[1] == "file":
          fname = command[2]
          length = command[3]
          length = int(length)
          print(genfile("predefined", fname, length))
    elif usrwords[0] == "exit":
      break
    else:
      print("Unknown command: " + usrwords[0])


if __name__ == "__main__":
    main()