# Word Dictionary
from PyDictionary import PyDictionary

dictionary = PyDictionary()

print(dictionary.meaning("Boxer"))
 
 
def main():
    word_dictionary = {
        "Hi" : "A way of greeting.",
        "Eyes" : "An organ for sight.",
        "Earth" : "A planet in space."
        
    }
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])
main()


