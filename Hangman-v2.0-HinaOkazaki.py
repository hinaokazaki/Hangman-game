#########################################################################
#
#  Python Project - Hangman Original
#
#  File:       Project/Hangman-v1-5.py
#  Project:    Final assesment
#  Author:     Hina Okazaki (20077851@tafe.wa.edu.au)
#  Copyright:  © Copyright 2022, Hina Okazaki
#
#########################################################################
#
# importing modules
# import only system from os
from os import system, name
# import sleep to show output for some time period
import time
# import os path
import os.path
# import random
import random
#
#########################################################################
# CONSTANTS
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

HARD_LIVES = 8
NORMAL_LIVES = 10
EASY_LIVES = 13
SCORE_AMOUNT = 10

##########################################################################
# INPUT FUNCTIONS

def askUserForSingleCharacter(options=[], prompt="Enter a character"):
    choice = ""
    if len(options) == 0:
        options = ALPHABET
    optionsList = ",".join(options)
    while options.count(choice) <= 0:
        print("Options are: " + optionsList)
        choice = input(prompt + ": ")
        if options.count(choice) <= 0:
            print("OOPS! You made an error...")
        #end if
    #end while
    return choice

##########################################################################
# UTILITY FUNCTIONS
#
# define the clear screen function
def clearScreen():
    # for Windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux (here os.name is 'posix')
    else:
        _ = system('clear')
#
# Display a line of characters with end characters different if required
def displayLine(char="=", lineLength=10, endChar="*"):
    print(endChar + char * (lineLength - len(endChar) * 2) + endChar)
#
#
#########################################################################
# WELCOME USER FUNCTION
#
# getPlayerName function - generic code Service Request No. 1 (30/05/2022) Enhancement #1
def getPlayerName(gameName,gameVersion):
    # Display game Title
    print("="*40)
    print("   Simple Games Collective presents...")
    print("   ",gameName, "- Version",gameVersion)
    # Prompt for Player name
    string=input("Please enter your Player name: ")
    # if player name is blank, display error message and reprompt
    while string=="":
        print("Player name must not be blank.")
        string=input("Please enter your Player name: ")
    # end while
    # acknowledge player
    print("")
    print("Welcome "+string+", I hope you enjoy this game with me.")
    # return player name to calling program
    return string
# end def getPlayerName

#########################################################################
# MENU FUNCTION
#
def showMenu(menuWidth=60, menuLines=[]):
    clearScreen()
    insideWidth = menuWidth - 4
    displayLine("-", menuWidth, "+")
    for aMenuLine in menuLines:
        print("| {1:{0}} |".format(insideWidth, aMenuLine))
    displayLine("-", menuWidth, "+")
# end showMenu

def askUserForChoice(validChoices):
    choice = ""
    # while choice not in valid chars:
    while choice not in validChoices:
        choice = input("Please select the level of difficulity : ")
        if choice in validChoices:
            break
        else:
            print("OOPS! Your choice is not valid! Try again!")
        # end if
    #end while
    return choice
# end askUserForChoice

#########################################################################
# MAIN FUNCTION HARD LEVEL
#
def mainHard():
    time.sleep(1.0)
    print("Start guessing...")
    time.sleep(0.5)
    displayLine("=", 80, "=")

    # here we set the secret word - in the project you need to amend this to
    # open the default file and extract a list of words, and randomly select
    # from that list.
    word = x

    # create a guesses variable with an empty value
    guesses = ''

    # create a variable for the score
    score = 0

    # determine the number of lives
    lives = HARD_LIVES

    # list of letters not used
    letters = ALPHABET

    # Create a while loop
    # check if the lives are more than zero
    while lives > 0:
        # make a counter that starts with zero
        failed = 0

        print("\nGuess the word: ", end="")
        # for every character in the secret word
        for char in word:
            # see if the character is in the players guesses
            if char in guesses:
                # print then out the character
                print(char, end="")
            else:
                # if not found, print a dash
                print("-", end="")
                # and increase the failed counter by one
                failed += 1
        #if failed is equal to zero
        # print You Won
        if failed == 0:
            print("\nYou won")
            # exit the script
            break

        print("\n\n")
        # ask the user to guess a character
        guess = askUserForSingleCharacter(letters, "Enter a character")
        # add the guess to the list of characters used so far...
        guesses += guess

        # remove the guess from the list of available letters
        letters.remove(guess)

        # if the guess is not found in the secret word
        if guess not in word:
            # lives counter decreases by 1
            lives -= 1
            # print wrong
            print("Guessed Wrong!\n")
        else:
            # increase the player score
            score = score + SCORE_AMOUNT

        # how many lives are left
        print("You have", + lives, 'more guesses\n')

        # if the lives are equal to zero
        if lives == 0:
            # print "You Lose"
            print("You Lose")
            
    # Press enter to quit
    finish = input("Press enter to finish. Goodbye " + playerName)


#########################################################################
# MAIN FUNCTION NORMAL LEVEL
#
def main():
    time.sleep(1.0)
    print("Start guessing...")
    time.sleep(0.5)
    displayLine("=", 80, "=")

    # here we set the secret word - in the project you need to amend this to
    # open the default file and extract a list of words, and randomly select
    # from that list.
    word = x

    # create a guesses variable with an empty value
    guesses = ''

    # create a variable for the score
    score = 0

    # determine the number of lives
    lives = NORMAL_LIVES

    # list of letters not used
    letters = ALPHABET

    # Create a while loop
    # check if the lives are more than zero
    while lives > 0:
        # make a counter that starts with zero
        failed = 0

        print("\nGuess the word: ", end="")
        # for every character in the secret word
        for char in word:
            # see if the character is in the players guesses
            if char in guesses:
                # print then out the character
                print(char, end="")
            else:
                # if not found, print a dash
                print("-", end="")
                # and increase the failed counter by one
                failed += 1
        #if failed is equal to zero
        # print You Won
        if failed == 0:
            print("\nYou won")
            # exit the script
            break

        print("\n\n")
        # ask the user to guess a character
        guess = askUserForSingleCharacter(letters, "Enter a character")
        # add the guess to the list of characters used so far...
        guesses += guess

        # remove the guess from the list of available letters
        letters.remove(guess)

        # if the guess is not found in the secret word
        if guess not in word:
            # lives counter decreases by 1
            lives -= 1
            # print wrong
            print("Guessed Wrong!\n")
        else:
            # increase the player score
            score = score + SCORE_AMOUNT

        # how many lives are left
        print("You have", + lives, 'more guesses\n')

        # if the lives are equal to zero
        if lives == 0:
            # print "You Lose"
            print("You Lose")
            
    # Press enter to quit
    finish = input("Press enter to finish. Goodbye " + playerName)

#########################################################################
# MAIN FUNCTION EASY LEVEL
#
def mainEasy():
    time.sleep(1.0)
    print("Start guessing...")
    time.sleep(0.5)
    displayLine("=", 80, "=")

    # here we set the secret word - in the project you need to amend this to
    # open the default file and extract a list of words, and randomly select
    # from that list.
    word = x

    # create a guesses variable with an empty value
    guesses = ''

    # create a variable for the score
    score = 0

    # determine the number of lives
    lives = EASY_LIVES

    # list of letters not used
    letters = ALPHABET

    # Create a while loop
    # check if the lives are more than zero
    while lives > 0:
        # make a counter that starts with zero
        failed = 0

        print("\nGuess the word: ", end="")
        # for every character in the secret word
        for char in word:
            # see if the character is in the players guesses
            if char in guesses:
                # print then out the character
                print(char, end="")
            else:
                # if not found, print a dash
                print("-", end="")
                # and increase the failed counter by one
                failed += 1
        #if failed is equal to zero
        # print You Won
        if failed == 0:
            print("\nYou won")
            # exit the script
            break

        print("\n\n")
        # ask the user to guess a character
        guess = askUserForSingleCharacter(letters, "Enter a character")
        # add the guess to the list of characters used so far...
        guesses += guess

        # remove the guess from the list of available letters
        letters.remove(guess)

        # if the guess is not found in the secret word
        if guess not in word:
            # lives counter decreases by 1
            lives -= 1
            # print wrong
            print("Guessed Wrong!\n")
        else:
            # increase the player score
            score = score + SCORE_AMOUNT

        # how many lives are left
        print("You have", + lives, 'more guesses\n')

        # if the lives are equal to zero
        if lives == 0:
            # print "You Lose"
            print("You Lose")
            
    # Press enter to quit
    finish = input("Press enter to finish. Goodbye " + playerName)

#########################################################################
# THE MAIN PROGRAM
#########################################################################
clearScreen()
displayLine("-", 80, "-")



# Initialise game and get Player Name
gameName = "Hangman Game"
gameVersion = "2.0"
playerName = getPlayerName(gameName,gameVersion)

# wait for 1 second
time.sleep(1)

# Display game play instructions
print("In this game I am thinking of a random word.")
print("You have up to 8 to 13 guesses to try to guess what that word is.")
print("And it is depend on the level you choose.")
time.sleep(0.5)
print("Good luck!")
print(" ")
time.sleep(0.5)

displayLine("-", 80, "-")

# ask file name to choose random word
while True:
        answer = input("Enter the file name: ")
        if answer == "default.txt":
            with open("./word-lists/default.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                x = random.choice(words)
                # print(x)
                break
        else:
            responce = input("That file is not exist, enter the file name again: ")
            if responce == "default.txt":
                with open("./word-lists/default.txt", "r") as file:
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    x= random.choice(words)
                    # print(x)
                    break


# set up predetermined list of menu choices
choices = ["0","1","2","3",]
# set menu options
myMenu = [
        "Menu - Please make your choice ",
        " ",
        "1) Hard",
        "2) Normal",
        "3) Easy",
        " ",
        "0) Quit"
    ]

# Start up sequence...
clearScreen()
print("Starting up....")
time.sleep(2)


# display the menu and process choice
showMenu(40, myMenu)
menuChoice = askUserForChoice(choices)
print()

while menuChoice != "0":
    if menuChoice == "1":
        print("Well done, you picked hardest one.")
        print("You have only 8 lives to play the game")
        mainHard()
        break
    elif menuChoice == "2":
        print("Enjoy the normal level!")
        print("You have 10 lives to guess word.")
        main()
        break
    elif menuChoice == "3":
        print("You chose easy one! It is good to start the game!")
        print("You have 13 lives to play this game.")
        mainEasy()
        break
    else:
        print("That is a valid choice. You can only choose from the menu.")
        break
    # end if
    
# end while
