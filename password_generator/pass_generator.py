# Ask if the user wants to generate a password
# If Yes, password length
# Generate password, print the password
# If no, exit the program

import string
import random

chars = list(string.ascii_letters + string.digits + "!@$%^&*()")


def generate_password():
    pass_len = int(input("How long would you like your password to be? "))
    random.shuffle(chars)
    password = []

    for x in range(pass_len):
        password.append(random.choice(chars))

    random.shuffle(password)
    password = "".join(password)
    print(password)


option = input("Want to generate a password? (Yes/No): ")
if option == "Yes":
    generate_password()
elif option == "No":
    print("Program Ended!")
    quit()
else:
    print("Invalid Input!!")
    quit()
