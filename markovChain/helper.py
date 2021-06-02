from itertools import tee

class helper:
  def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
  
  def convert_to_list(worddict, lastword):
    choosablewords = []
    for k, v in worddict[lastword].items():
      for i in range(v):
        choosablewords.append(k)
    return choosablewords
  
  def file_to_one_line(filename):
    try:
      with open(filename, "r") as f:
        filedata = f.read()
      mylist = [item for item in filedata.split('\n')]
      newstring = ' '.join(mylist)
      with open(filename, "w") as f:
        f.write(newstring)
    except FileNotFoundError:
      print("File does not exist")