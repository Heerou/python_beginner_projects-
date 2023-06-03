# create a dictionary that has a key value that represents a word, and it's definition
# get the input from the user
# check if the word it's in the dictionary and print the definition

from PyDictionary import PyDictionary

the_dictionary = PyDictionary()

#
# def main():
#     dictionary = {
#         'hi': 'hello',
#         'eyes': 'what you use to see',
#         'earth': 'where you live'
#     }
#
#     while True:
#         word = input("Please type a word: ")
#         if word == "":
#             break
#         if word in dictionary:
#             print(word, ":", dictionary[word])

while True:
    word = input("Please type a word: ")
    if word == "":
        break

    print(the_dictionary.meaning(word))
