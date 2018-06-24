"""
Created on Sun Jun  3 18:19:42 2018

@author: bjwil
Assignment #6 - Dice Rolling Simulator
"""
      
#import random for roll function, statistics for mean, time for rolling time
import random
import statistics as stat
import time

#function for random roll of dice.  List is for a 6-side die.
def roll(num_of_dice):
    number = [1, 2, 3, 4, 5, 6]
    rolledNumbers = []
    for i in range(0,num_of_dice):
        rolledNumbers.append(random.choice(number))
    # return list of numbers
    return rolledNumbers

#prompt roller if they would like to roll the dice. Y/N only valid answers.
continue_Rolling = input("Would you like to roll the dice? Enter (Y/N)\n").upper()

#if user does not enter Y/N continues to prompt until Y/N is entered
while continue_Rolling not in ['Y', 'N']:
    print("Invalid entry! Please select (Y/N)\n")
    continue_Rolling = input("Would you like to roll the dice? Enter (Y/N)\n").upper()

#if user enters N quit the game.   
if continue_Rolling == 'N':
    print("Thanks.  Maybe next time.")
    play = False
#else play on
else:
    play = True

#initiate number of rolls, what the last roll was, word for rolls left, and score for average roll
number_of_Rolls = 0
last_Roll = 0
word = 'rolls'
average_Roll = 0

#give user 5 rolls
while number_of_Rolls < 5 and play:
    #continue to prompt user to interger amount of dice. throw error if not an integer input and prompt again.
    while True:
        try:
            how_Many_Dice = int(input("How many dice would you like to roll?\n"))
            break
        except ValueError:
            print("Int, please.")
    #text to mimic rolling of dice
    text = ("Rolling... Rolling... Rolling... Rolling... Stopped...")
    #loop text to mimic the rolling
    for rolling in text.split():
        print(rolling), time.sleep(0.5)
    #increase number of rolls
    number_of_Rolls += 1
    #run roll function to get random roll results
    dice_rolled = roll(how_Many_Dice)
    #print roll number and output of roll
    print('Roll {}: {}'.format(number_of_Rolls, ', '.join(map(str,dice_rolled))))
    #average the roll
    average_Roll = round(stat.mean(dice_rolled),2)
    #print the average
    print('Your average roll was {}.'.format(average_Roll))
    #text for first roll if it was greater than mean of a die roll (mean is 3.5)
    if number_of_Rolls == 1:
        if average_Roll > 3.5 and average_Roll < 6:
            print("Not bad for a first roll.")
    #if more than one roll continue to measure against last roll
    if number_of_Rolls > 1:
        #if average of roll was higher than last roll print text
        if average_Roll > last_Roll and average_Roll < 6:
            print("Good job. You beat your last roll.")
        #else print roll was lower than last roll. if roll was same as average print nothing
        elif average_Roll < last_Roll:
            print("Your last roll was higher.  Maybe you should have quit while you were ahead.")
    #initiate last roll to equal the last roll that just occured for next roll comparison
    last_Roll = average_Roll
    #break loop if average was 6 since you cannot beat 6.
    if average_Roll == 6:
        print("What a roll! I'm going to stop you now because you are hot!")
        break
    #slow output for user to read
    time.sleep(0.5)
    #prompt user if they would like to roll again
    if number_of_Rolls < 5:
        if 5-number_of_Rolls == 1:
            word = 'roll'
        roll_Again = input("Would you like to roll again and beat your score? You have {} {} left.\n".format(5-number_of_Rolls, word)).upper()
    #if user does not enter Y/N continues to prompt until Y/N is entered
    while roll_Again not in ['Y', 'N']:
        print("Invalid entry! Please select (Y/N)")
        roll_Again = input("Would you like to roll again and beat your score?\n").upper()
    # break loop if user wants to end before 5 rolls
    if roll_Again == 'N':
        print("Thanks for playing!\n")
        break

#if user played the game
if play:
    #if user decided to stop before 5 rolls print results of rest of rolls
    if 5-number_of_Rolls > 0:
        print("Here is what the rest of your rolls would have been with the same amount of dice as your last roll:\n")
        #increase for next roll
        number_of_Rolls += 1
        #loop through rest of rolls
        for i in range(0,5-number_of_Rolls+1,1):
            dice_rolled = roll(how_Many_Dice)
            print('Roll {}: {} Average: {}'.format(number_of_Rolls, ', '.join(map(str,dice_rolled)), round(stat.mean(dice_rolled),2)))
            number_of_Rolls += 1
    #print final results
    if average_Roll >= 5:
        print("Your final score was {}. You're a star!  Thanks for playing!".format(average_Roll))
    elif average_Roll > 3.5 and average_Roll < 5:
        print("Your final score was {}. You scored above average.  Thanks for playing!".format(average_Roll))
    elif average_Roll == 3.5:
        print("Your final score was {}. You scored the average.  Thanks for playing!".format(average_Roll))
    elif average_Roll > 2 and average_Roll <= 3.5:
        print("Your final score was {}. You scored below average.  You should think about playing again.".format(average_Roll))
    else:
        print("Your final score was {}. You did not score well.  You should think about playing again.".format(average_Roll))
    



