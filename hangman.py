#
import random

print("")
print("~ WELCOME TO HANGMAN ~")
print("")

word_list = ["school", "flowers", "Canada", "movies", "Food"]
word = str(random.choice(word_list))
length = len(word)
lives = length + 3
correct_guesses = 0
list_of_letters = list(word)

print("A word has been selected. The word has", length, "letters and you have ", lives, "guesses.")

while lives > 0:
    letter = str(input("Enter a guess: "))
    lives = lives -1
    if letter in list_of_letters:
        correct_guesses = correct_guesses +1
        list_of_letters.remove(letter)
        print("Correct guess!", letter, "is in the word!")
        if correct_guesses == length:
            print("You win! You guessed <", word, "> correctly!!")
print("You've ran out of lives. The word was:", word)
