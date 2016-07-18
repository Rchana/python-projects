#Hangman Game
import random

print("")
print("~ WELCOME TO HANGMAN ~")
print("")

yes_no = "yes"

while yes_no == "yes":
    word_list = ["school", "flowers", "Canada", "movies", "Food"]
    word = str(random.choice(word_list)).lower()
    length = len(word)
    lives = length + 3
    correct_guesses = 0
    list_of_letters = list(word)

    print("")
    print("A word has been selected. The word has", length, "letters and you have", lives, "guesses.")
    print("")
    while lives > 0:
        print("")
        print("You have", lives, "lives left.")
        letter = str(input("Enter a guess: "))
        lives = lives -1
        if letter in list_of_letters:
            correct_guesses = correct_guesses +1
            while letter in list_of_letters:
                list_of_letters.remove(letter)
            print("Correct guess!", letter, "is in the word!")
            if len(list_of_letters) == 0:
                print("")
                print("You win! You guessed <", word, "> correctly!!")
                break
            elif lives == 0 and len(list_of_letters) != 0:
                print("You've ran out of lives. The word was:", word)
        elif lives == 0 and len(list_of_letters) != 0:
            print("You've ran out of lives. The word was:", word)
    print("")
    yes_no = str(input("Do you want to play again? ")).lower()
