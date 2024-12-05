from random import *

#computer choses a number from 1-6
ranumb=randint(1, 6)
#user inputs a number from 1-6
usernumb=int(input("Guess a number from 1-6: "))
#if the nubmber is the same as the computer's number, the user wins
if ranumb==usernumb:
  print("You win!")
#if the number is different then the computers number, the user loses
if ranumb!=usernumb:
  print("you lose")  
