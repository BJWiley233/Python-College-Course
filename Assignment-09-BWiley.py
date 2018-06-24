# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 06:19:05 2018

@author: bjwil
Assignment #9 Guessing Game
"""

import random
import sys

# uses a different string "...again" rather than the initial string that firsts asks to guess a number
def guessAgainQuestion(low, high):
     while True:
        try:
            input1 = input("Guess again and I will tell you if it's higher or lower (or presss q/Q to quit): ")
            if input1.isalpha() and input1.upper() == 'Q' or input1.upper() == 'q':
                sys.exit()
            else:
                input1 = int(input1)
        except ValueError:
            print("That was not an integer.  Please select and integer between 1 and 100.")
        else:
            if input1 in range(low, high + 1):
                return input1
            print("Out of range.  Please select and integer between 1 and 100.")
            
# main function to start off the game and to compare if guess is higher or lower       
def main(gamesPlayed, low = 1, high = 100):
    # if its the first game played, introduce the game and the goal with a hint
    if gamesPlayed < 1:
        print("I'm thinking of a number between {} and {}.".format(low, high))
        print("Can you guess my number?  I will give you 20 tries but it should take you no more than 7.")
        print("Copy this link for a hint into a browser:\nhttps://math.stackexchange.com/questions/512994/guessing-a-number-between-1-and-100-in-7-guesses-or-less")
    
    # a random number will be generated each time the game/main method is played
    actualNumber = int(random.choice(range(low, high+1))) 
    # instantiate variable for count number of tries/guesses
    tries = 0
    # ending for number of tries so to change ending if guess is correct on 1st, 2nd, or 3rd try
    word = 'th'
    # as user to make first guess
    while True:
        try:
            input1 = input("Guess a number and I will tell you if it's higher or lower (or presss q/Q to quit): ")
            # if user enters any letter other than only q or Q, it will print the exception, otherwise q or Q will quit program
            if input1.isalpha() and input1.upper() == 'Q' or input1.upper() == 'q':
                sys.exit()
            # if input is not q, Q, or another string, i.e. it's a number, then coerce to an integer data type to make the exception work
            else:
                input1 = int(input1)
        #
        except ValueError:
            print("That was not an integer.  Please select and integer between 1 and 100.")
        # else if not "q/Q" for quit and is an integer
        else:
            # if input integer is in the valid range break to exit while loop
            if input1 in range(low, high + 1):
                break
            # else print out of range and continue with while loop to ask for valid input range
            print("Out of range.  Please select and integer between 1 and 100.")
    
    # while guess is less than 20        
    while tries < 20:
        # increase try
        tries += 1
        # if guess from user equals the actual randon number generated, if the tries are 3 or less change ending, 
        # print final statement and break the while loop which will end the main function
        if input1 == actualNumber:
            if tries == 1:
                word = 'st'
            elif tries == 2:
                word = 'nd'
            elif tries == 3:
                word = 'rd'
            print("Wow!  You got it on the {}{} try!".format(tries, word))
            gamesPlayed += 1
            break
        # if the input from user is higher than the random number, tell user to guess lower
        if input1 > actualNumber:
            print("Lower\n")
            input1 = guessAgainQuestion(low, high)
        # if the input from user is lower than the random number, tell user to guess higher            
        else:
            print("Higher\n")
            input1 = guessAgainQuestion(low, high) 

# instantiate number of games play variable for the introduction, after 1 game will no longer introduce game
gamesPlayed = 0
# start to play once program is ran
play = True

# while user continues to play 
while play == True:
    # call main function to play a game based on how many have been played already
    main(gamesPlayed)
    # increase count for number of games played
    gamesPlayed += 1
    # once main function ends create dict of valid answers for when asked to play again
    valid = {"YES": True, "Y": True, "NO": False, "N": False}
    # ask to play again
    playAgain = str(input("Play again (Y/N)? ").upper())
    # while the entry from the user is not valid, continue to prompt for valid input
    while playAgain not in valid:
        playAgain = str(input("Invalid. Please enter (Y/N): ").upper())
    # if play again is valid selection, play will equal True or False 
    if playAgain in valid:
        play = valid[playAgain]
    # before breaking while loop and ending program completely if input is a key for False value, print thanks statement
    if play == False:
            print("Thanks for Playing!")

# will also work with any other gap but the introduction does not change.           
# main(gamesPlayed, low = 1, high = 128)
