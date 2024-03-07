path = "books/frankenstein.txt"

def openfile():
    with open(path,'r') as file:
        return file.read()
    
def count_words():
    words = openfile().split()
    return len(words)

def count_letters():
    book = openfile().lower()
    letters = {}
    for letter in book:
        if letter.isalpha():
            if letter in letters:
                letters.update({letter:letters[letter]+1})
            else:
                letters[letter]= 1
    return letters.items()

def report():
    print(f"----Begin report for {path} ----\n{count_words()} words in this document \n")
    for letter, count in sorted(count_letters()):
        print(f" - The letter {letter} was used {count} times mad right? - \n")

def main():
    report()

if __name__ == "__main__":
    main()