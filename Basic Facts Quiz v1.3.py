#Importing my external file that contains my questions
from data import data
import random

#Defining the Functions
def gamestart():
    print("Welcome to the quiz, you will be asked to solve multiple questions, each time you do the quiz, you will keep answering questions till you get 1 wrong.")
    print("Answer the questions using the corresponding numbers from 1 to 4")
    print("Good Luck!")

score = 0
def addscore():
    global score
    if score >= 3:
        score = score + (score - 1)
    else:
        score = score + 1

def resetscore():
    global score
    score = score - score

def minusscore():
    global score
    score = score - 1

def maingame():
    question = random.choice(data)
    print(question["question"])
    print(question["option1"])
    print(question["option2"])
    print(question["option3"])
    print(question["option4"])
    print("Please choose a number 1 - 4 that matches the 4 choices")
    while True:
        try:
            userchoice = int(input(""))
            break
        except:
            print("Please input a number from 1 - 4 only")
    if userchoice == question["answer"]:
        print("Correct, Current score: {}".format(score))
        addscore()
        maingame()
    else:
        print("Incorrect")
        print(f"The real answer is {question['answer']}")
        print(f"Your final score was {score}")
        resetscore()
        while True:
            playagain = int(input("Play again? 1 = Yes, 2 = No: "))
            if playagain == 1:
                gamestart()
                maingame()
            else:
                exit()

#Introduces my Quiz 
print("Welcome to my Basic Facts Quiz!!")
print("In order for us to allow you to take the quiz, we need to check if you are eligible by asking you a few questions")

#Behind the Filtering Process
name = input("What is your name? ")
print("Thats crazy {}" .format(name.capitalize()))

#Asks the question and forces a integer Value
while True:
    try:
        age = int(input("What is your age? "))
        break
    except:
        print("Please input a number only")

#The Age range to complete filtering process
if age >= 13:                                     
    print("Congratulations you are elgible for this quiz!")
    resetscore()
    gamestart()
    maingame()
if age <= 12:
    print("You are too young for this basic facts quiz")
    exit()