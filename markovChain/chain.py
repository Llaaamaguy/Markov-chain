import random
from .helper import helper


class Chain:
  def generate_dict(userinput):
    words = userinput.split(" ")
    worddict = {}
    for i, j in helper.pairwise(words):
      if i in worddict:
        if j in worddict[i]:
          worddict[i][j] += 1
        else:
          worddict[i][j] = 1
      else:
        worddict[i] = {j: 1}
    return worddict

  def generate_bad_text(worddict, length):
    string = [random.choice(list(worddict.keys()))]
    for i in range(length):
      lastword = string[i-1]
      if lastword not in worddict:
        string.append(random.choice(list(worddict.keys())))
      else:
        choosablewords = helper.convert_to_list(worddict, lastword)
        string.append(random.choice(choosablewords))
    return string
  
  