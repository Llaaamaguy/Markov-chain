from itertools import tee
import random

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
    
def generate_text(worddict):
  """
  generate text using mArKoV cHaIn
  """

def generate_bad_text(worddict):
  length = 50
  string = []
  for i in range(length):
    if i == 0:
      string.append(random.choice(list(worddict.keys())))
    else:
      lastword = string[i-1]
      string.append(random.choice(list(worddict[lastword].keys())))
  return string

def main(): 
  while True:
    #Im gonna try making the UI like a command line because why not
    usrinput = input("markov_chain_project: ")
    usrwords = usrinput.split()
    if usrwords[0] == "help":
      print('START    Starts the training process \n [type]                  [file]\ntype in custom text     get text from a file\n\nEXIT     Exits the program')
    elif usrwords[0] == "start":
      if usrwords[1] == "type":
        print('\n')
        string = input("What is your training input: ")
        worddict = generate_dict(string)
        print(worddict)
        generated = generate_bad_text(worddict)
        print(generated)
      elif usrwords[1] == "file":
        print('\n')
        fname = input("File name: ")
        try:
          with open(fname, "r") as f:
            text = f.read()
          worddict = generate_dict(text)
          generated = generate_bad_text(worddict)
          print(" ".join(generated))
        except FileNotFoundError:
          print("File did not exist")
    elif usrwords[0] == "exit":
      break


if __name__ == "__main__":
    main()