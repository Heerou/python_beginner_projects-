# A dictionary that store questions and answers
# have a var that tracks the score
# loop through the dictionary using key values
# display the questions allow them to answer
# tell them if they're right or wrong
# show them the final result

# dictionary
the_quiz = {
    "Question_1": {
        "question": "Whats the capital of Paris?",
        "answer": "Paris"
    },
    "Question_2": {
        "question": "Whats the capital of Germany?",
        "answer": "Berlin"
    },
    "Question_3": {
        "question": "Whats the capital of Italy?",
        "answer": "Rome"
    },
    "Question_4": {
        "question": "Whats the capital of Spain?",
        "answer": "Madrid"
    },
    "Question_5": {
        "question": "Whats the capital of Portugal?",
        "answer": "Lisbon"
    },
    "Question_6": {
        "question": "Whats the capital of Switzerland?",
        "answer": "Bern"
    }
}

score = 0

for key, value in the_quiz.items():
    print(value['question'])
    ans = input("Answer? ")

    if ans.lower() == value['answer'].lower():
        print("Correct!! ")
        score += 1
        print("Your score is: ", str(score) + "\n")
    else:
        print("Wrong!! ")
        # score -= 1
        print("The real answer is: ", str(value['answer']))
        print("Your score is: ", str(score) + "\n")

print("You got: " + str(score) + " out of " + str(len(the_quiz)) + " correctly")
print("You  percentage is: " + str(score / len(the_quiz) * 100) + "%")
