#Importing my external file that contains my questions
from data import data
import random

#Introduces my Quiz 
print("Welcome to my Basic Facts Quiz!!")
print("In order for us to allow you to take the quiz, we need to check if you are eligible by asking you a few questions")

#Behind the Filtering Process
name = input("What is your name? ")
print("Thats crazy {}" .format(name.capitalize()))

while True:
    try:
        age = int(input("What is your age? "))
        break
    except:
        print("Please input a number only")

#The Age range to complete filtering process
if age >= 13:
    print("Congratulations you are elgible for this quiz!")
if age <= 12:
    print("You are too young for this basic facts quiz")
    exit()

