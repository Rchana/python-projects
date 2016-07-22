# The following code checks whether entered input is a palindrome

play = "y"

while play == "y":
    userInput = input("Please enter your palindrome: ").casefold()
    reversedUserInput = reversed(userInput)
    if list(userInput) == list(reversedUserInput):
        print("This is a palindrome!")
    else:
        print("This is not a palindrome.")
    print("")
    play = input("Would you like to check another input [Y/N]?").lower()
