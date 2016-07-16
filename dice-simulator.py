#Random dice number generator

import random

#save the users input
dice = input("Would you like to roll a dice? ").lower()

#check whether the user wants to roll the die
while dice == "yes" or dice == "y":
    print("Your random number is...")
    #output the random number
    print(random.randint(1,6))
    #ask the user whether they would like to roll again
    dice = input("Would you like to roll again? ").lower()
