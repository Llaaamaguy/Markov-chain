from .chain import Chain

class generate:
  def gencustom():
    string = input("What is your training input: ")
    length = int(input("Length of output: "))
    worddict = Chain.generate_dict(string)
    generated = Chain.generate_bad_text(worddict, length)
    return(" ".join(generated))
  
  def genfile(mode, fname=None, length=None):
    if mode == "nondefined":
      fname = input("File name: ")
      length = int(input("Length: "))
      with open("lastcommand.txt", "a") as f:
        f.write(fname + " " + str(length) + "\n")
    try:
      with open(f"textFiles/{fname}", "r") as f:
        text = f.read()
      worddict = Chain.generate_dict(text)
      generated = Chain.generate_bad_text(worddict, length)
      return(" ".join(generated))
    except FileNotFoundError:
      return("File did not exist")