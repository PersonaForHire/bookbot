path = "books/frankenstein.txt"

def openfile():
    with open(path,'r') as file:
        return file.read()
def count_words():
    words = openfile().split()
    print(len(words))

def main():
   # print(openfile())
    count_words()

if __name__ == "__main__":
    main()

