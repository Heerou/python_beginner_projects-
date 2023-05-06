def replace_words():
    the_string = "Well this a sting that has to be replaced"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(the_string.replace(word_to_replace, word_replacement))


replace_words()
