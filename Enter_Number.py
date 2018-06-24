# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 07:35:46 2018

@author: bjwil
"""
# import sys for exit fuctionality
import sys
# import string for ascii alphabet
import string
# import pandas to review results in a dataframe
import pandas as pd

# initialize alphabet variable
alphabet = string.ascii_uppercase
# number of letters in alphabet for string to int function and int to string function
n = len(alphabet)
# create dictionary and assign number 1-26 to each letter of alphabet
values = dict()
for index, letter in enumerate(alphabet):
    values[letter] = index + 1    
    
# main function for assignment.  I probably could have used the try/except under function longer_string_to_int()
# but I wanted to have differnt answers and to use the KeyError I would need to remove A and Z from the values dictionary
# which would have been easy actually but chose this instead          
def question(starting_letter = 'B', ending_letter = 'Y'):
    # prompt user for input and coerce to uppercase for dictionary values
    letter_entered = input("Please enter a letter including and between B and Y or hit 'Enter' to exit. ").upper()
    # system will exit if use hits enter
    if not letter_entered:
        sys.exit()
    # if entry is a number or len is greater than 1, require correct input
    while letter_entered.isdigit() or len(letter_entered) > 1:
        letter_entered = input("Please enter one (1) valid LETTER between B and Y. ").upper()
        if not letter_entered:
            sys.exit()
    # if entry is 'A' or 'Z', require input between 'B' and Y'
    while values[letter_entered.upper()] not in range(values[starting_letter], values[ending_letter] + 1):
        letter_entered = input("Out of range! Please enter a valid letter between B and Y. ").upper()
        # if user enters 'A' or 'Z' first, must include a while loop again for invalid entries
        while letter_entered.isdigit() or len(letter_entered) > 1:
            letter_entered = input("Please enter one (1) valid LETTER between B and Y. ").upper()
        if not letter_entered:
            sys.exit()         
    # return letter entered
    return letter_entered

# def for numbering strings with more than one letter    
def longer_string_to_int():
    ''' found in source below:
        https://codereview.stackexchange.com/questions/182733/base-26-letters-and-base-10-using-recursion
        
        This code allow numbering strings based on the basis of shortest string must be counted before longer
        strings. i.e. we must count all 2 letter strings AB...BA...QP...ZZ before three letter strings AAA...ABA.  
        
        Function clarity: 'ZZ' would be 702 and 'AAA' would be 703 instead of 3 for 1-1-1 or 53 for 1-27-53 
        which are really valuing string techniques and not counting sequence.
            'ZZ' is comprised multiplying 26^len('ZZ') + 26^(len('ZZ')-1) or 26**2 + 26**1 = 702
            'ZZZ' is comprised multiplying 26^len('ZZZ') + 26^(len('ZZZ')-1) or 26**3 + 26**2 = 18252
            'AAA' is comprised of (((0 * 26 + 1) * 26 + 1) * 26 + 1) = 703
    '''
    # while loop to keep asking input if input is valid
    while True:
        number = 0
        string = input("Please enter a word with no spaces or numbers or hit 'Enter' to exit'. " )
        if not string:
            sys.exit()
        try:
            # for each letter in the string as an uppercase letter, must coerce to uppercase for valid key in values dict
            for char in string.upper():
                # this provides the 'recursion' functionality but not really recursion of def rather recursion of loop
                number = number * n + values[char]
            return number
    # raises key error if entry is not a str
    # see type(list(values.keys())[0]) = str
        except KeyError:
            print("Input can only contain letters.")
            #raise ValueError("Input can only contain letters.")

# def for converting number to integers
def int_to_string(number):
    ''' found in source below:
        https://codereview.stackexchange.com/questions/182733/base-26-letters-and-base-10-using-recursion
        
        divmod() takes two numbers and returns a tuple that consists of the quotient and remainder.
        
        example divmod(53 - 1, 26) = (2, 0) will give an 'A' at the end and recurse the 2
        
        Function clarity: for any value which is multiple of 26 + 1, i.e. 53, 79, 261 will subtract 1 and
        have remainder of 0 which is the last letter of string and sufficed by adding 'A' to the end.  The beginning
        of the string is recursively concatenated with the function using the quotient
        Ex. 1:
            '261' will give remainder 0 and quotient 10 (returns 'A')
                '10' will give remainder 9 and quotient 0 (returns 'J' + 'A')
                Final return is 'JA'
        Ex. 2:
            '4644' will give remainder 15 and quotient 178 (returns 'P')
                '178' will give remainder 21 and quotient 6 (returns 'V' + 'P')
                    '6' will give remainder 5 and quotient 0 (returns 'F' + 'V' + 'P')
                    Final return is 'FVP'
        '''
    if number < 0:
        raise ValueError("Input a number greater than 0. Lowest integer of 1 is 'A'.")
    # when number = 0 means the last round of recursion only had a remainder so break and return
    if number == 0:
        return ''
    else:
        # need to subtract one since dictionary is indexed starting with 1 and alphabet is indexed starting at 0
        quotient, remainder = divmod(number - 1, n)
        # returns a quotient and remainder recursively
        return int_to_string(quotient) + alphabet[remainder]

# continue to play if True
play = True
# initialize dataframe for rounds of entries
data = pd.DataFrame(columns = ['Previous Letter:', 'Letter Entered:', 'Next Letter:'])
# dict for valid answers for playing again
valid = {"YES": True, "Y": True, "NO": False, "N": False}
# while play is true keep looping
while play == True:
    # entry equals function to ask question and returns a valid letter entered
    entry = question()
    # since the values dictionary is indexed starting with 1 and alphabet is indexed starting at 0 subtract 2 for previous letter
    previous_letter = alphabet[values[entry] - 2]
    # next letter just index alphabet with entered letter dictionary value. same reason as above
    next_letter = alphabet[values[entry]]
    # create dataframe will all three letters base on columns of initiliazed 'data' dataframe
    df = pd.DataFrame([[previous_letter, entry, next_letter]], columns = list(data))
    # append initalized dataframe with all three letters
    data = data.append(df, ignore_index = True)
    # ask user if they want to enter another letter
    playAgain = str(input("Would you like to enter another letter (Y/N)? ").upper())
    # if valid selection is made, the value from the key will determine if the while loop is True and continues or False or ends
    if playAgain in valid:
        play = valid[playAgain]
    # if keep prompting until valid entry
    while playAgain not in valid:
        playAgain = str(input("Invalid. Please enter (Y/N): ").upper())
    # break loop if user enters no
    if play == False:
            print("Thanks for Playing!\n")

# print results
print("Here are your results from your entries: \n")
print(data)
print('\n')

# do a fun bonus round for longer strings
print("Are you ready for the bonus round?")
# input calls string to int function
bonusEntry = longer_string_to_int()
# entry, previous, and next all call int to string
entry = int_to_string(bonusEntry)
previous_letter = int_to_string(bonusEntry - 1)
next_letter = int_to_string(bonusEntry + 1)
# same as above process for appending a dataframe however only allows for one entry, no while loop for play for bonus round
data = pd.DataFrame(columns = ['Previous Letter:', 'Letter Entered:', 'Next Letter:'])
df = pd.DataFrame([[previous_letter, entry, next_letter]], columns = list(data))
data = data.append(df, ignore_index = True)
print(data)

