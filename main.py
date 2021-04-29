from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def generate_dict(userinput):
    words = userinput.split()
    worddict = {}
    for i, j in pairwise(words):
        if worddict[i] == None:
            worddict[i] = {}
    print(worddict)
    
    

def main():
    usrinput = input("What is your string?: ")
    generate_dict(usrinput)

if __name__ == "__main__":
    main()