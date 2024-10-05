# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
from random import randint
from os import system
from time import sleep

def int_input(text: str) -> int:
    """
    Get console input with type of int, asks again if not correct type
    """
    while True:
        try:
            out: int = int(input(text))
            return out
        except ValueError:
            print("Incorrect type inputted, please input type: Int")


def display_question() -> bool:
    """
    Displays a random question and checks for correct answers.
    """
    number_1 : int = randint(0, 1000)
    number_2 : int = randint(0, 1000)

    answer : int = number_1 + number_2

    question : str = \
f"""  \t{number_1}
 +\t{number_2}
--------------------
"""
    out : int = int_input(question)
    # if incorrect display correct answer message and wait for any input to continue
    if out != answer: 
        # clear console
        system('cls')
        print("Incorrect answer!")
        print('-' * 20)
        print(f'Your answer: {out}\nCorrect answer: {answer}\n')
        # wait a little time to prevent accidental double tapping or enter key
        sleep(1)
        # wait for conformation
        input("Press Enter to continue...")

    return out == answer

# 10 question quiz
if __name__ == "__main__":
    answers_correct : int = 0
    for x in range(10):
        # clear console
        system("cls")
        # displays # of answers correct out of how many asked
        print(f"Answers correct: {answers_correct}/{x}")
        # 20 '-'
        print("-" * 20)
        # true = 1, false = 0. if question is wrong += 0 else += 1
        answers_correct += display_question()

    # clear console
    system('cls')

    print(f"Questions answered correctly: {answers_correct}/10")