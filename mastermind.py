'''
Created on Oct 21, 2017

@author: jon
'''

# Imports
import random

# Program Constants
NUMBER_OF_DIGITS = 4                # How many digits is the secret code?
MAX_DIGIT        = 6                # What is the largest digit we will use?
ALLOW_DUPES      = False            # Do we allow duplicates?
ALLOW_BLANKS     = 0                # Do we allow blanks?
MAX_GUESSES      = 12               # How many guesses do we allow?

# Globals
randomCode = []                     # The random code generated by the computer
userGuess  = []                     # What is the user's guess?


def generateRandomCode(size, max):
    """
    Generates a list containing random digits 
    :param size: how large is the list
    :param max: what is the largest integer in the list
    :returns: a list of integers
    """
    
    code = []
    blankAdd = 0                # Do we need spaces for blanks?

    # Loop through the length of the list and generate a random digit        
    while len(code) < size:
        digit = random.randint(1,max + blankAdd)
        if not ALLOW_DUPES:
            # If not, check if the number is already in the list
            # If it is, generate a new one until we get a unique number
            # Might want to change this to just add one until we get a unique number
            # This might cycle for a while otherwise
            while digit in code:
                digit = random.randint(1,max + blankAdd)
 
        code.append(digit)
    return code

def printIntroduction():
    print("MASTERMIND")
    print("----------")
    print()
    print("I have a secret number, consisting of " + str(NUMBER_OF_DIGITS) + " digits.")
    print("Each digit can be a number from 1 to " + str(MAX_DIGIT))
    if ALLOW_DUPES:
        print("Duplicate digits are allowed.")
    else:
        print("Duplicate digits are NOT allowed.")
    print("Your job is to guess the secret " + str(NUMBER_OF_DIGITS) + " code in " + str(MAX_GUESSES) + " turns or less.")
    print()
    print("Each time you guess, I will tell you if you got the code correct.")
    print("If not, I will tell you:")
    print("  - How many digits are correct, and in the right place, AND")
    print("  - How many digits are correct, but in the wrong place.")
    print()

# Checks if the user guessed the right code
# Prints out the clues if not
def check(code, guess):
    # If they didn't get it
    if (guess != code):
        print("Incorrect.")
        correctPlace=0
        correctDigit=0

        # Loop through the arrays
        for i in range(NUMBER_OF_DIGITS):
            # Check if the digit is in the right place
            if guess[i] == code[i]:
                correctPlace+=1
                
            # Now check if the digit is correct
            elif guess[i] in code:
                correctDigit+=1
            
        # Print the outcome
        print("  You have " + str(correctPlace) + " digits in the right place.")
        print("  And " + str(correctDigit) + " correct digits in the wrong place.")

def listify(myString):
    returnList = []
    for ch in myString:
        returnList.append(int(ch))
    return returnList

def main():
    """
    Main code
    """
    # Get the random code
    randomCode = generateRandomCode(NUMBER_OF_DIGITS, MAX_DIGIT)
    
    # What is the user's most recent guess?
    userGuessList = []
    
    # How many guesses has the user made?
    numGuesses = 0
    
    # Tell the user what's going on
    printIntroduction()
    
    # Loop while the user either:
    # a. Still has guesses left, and 
    # b. They have not guessed the secret code
    while numGuesses<MAX_GUESSES and randomCode != userGuessList:
        numGuesses += 1
        userGuess=""
        while len(userGuess) != 4:
            userGuess = input("Attempt " + str(numGuesses) + ": What is your guess: ")
        
        # Get the guess as a list
        userGuessList = listify(userGuess)

        # Check if they guessed correctly
        check(randomCode, userGuessList)
            
    # Print out whether they won or lost
    if numGuesses>MAX_GUESSES:
        print("Sorry - the secret code was " + randomCode)
    else:
        print("Congrats - you guessed it!")
        

# Kick out the jams!    
if __name__=="__main__":
    main()        
