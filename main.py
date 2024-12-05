from random import *

#computer choses a number from 1-6
ranumb=randint(1, 6)
#user inputs a number from 1-6
usernumb=int(input("Guess a number from 1-6: "))
if ranumb==usernumb:
  print("You win!")
if ranumb!=usernumb:
  print("you lose")  
