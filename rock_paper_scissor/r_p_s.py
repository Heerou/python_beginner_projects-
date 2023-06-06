import random

exit = False

while exit == False:
    options = ["rock", "paper", "scissor"]
    user_input = input("Choose rock, paper, scissors: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game Ended!")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It's a tie")
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer wins")
        elif computer_input == "scissor":
            print("Your input is rock")
            print("Computer input is scissor")
            print("You win")
    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You win")
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It's a tie")
        elif computer_input == "scissor":
            print("Your input is paper")
            print("Computer input is scissor")
            print("Computer wins")
    elif user_input == "scissor":
        if computer_input == "rock":
            print("Your input is scissor")
            print("Computer input is rock")
            print("Computer wins")
        elif computer_input == "paper":
            print("Your input is scissor")
            print("Computer input is paper")
            print("You win")
        elif computer_input == "scissor":
            print("Your input is scissor")
            print("Computer input is scissor")
            print("It's a tie")
    elif user_input != "scissor" or user_input != "rock" or user_input != "paper" or user_input != "exit":
        print("Invalid Input")
