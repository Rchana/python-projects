#Guess what number the random number generator generated between 1 ane 10

import random

number = random.randint(1,10)
guess = 0
while guess != number:
    guess = int(input("Take a guess: "))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
print("Right guess!")
