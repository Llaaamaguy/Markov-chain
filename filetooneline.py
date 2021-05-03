def main():
  while True:
    filename = input("File name: ")
    if filename == "exit":
      break
    try:
      with open(filename, "r") as f:
        filedata = f.read()
      mylist = [item for item in filedata.split('\n')]
      newstring = ' '.join(mylist)
      with open(filename, "w") as f:
        f.write(newstring)
    except FileNotFoundError:
      print("File does not exist")

if __name__ == "__main__":
  main()