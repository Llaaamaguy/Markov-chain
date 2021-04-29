from itertools import tee

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
  generate text
  """

def main():
    usrinput = input("What is your string?: ")
    worddict = generate_dict(usrinput)
    print(worddict)


if __name__ == "__main__":
    main()