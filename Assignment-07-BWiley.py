# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 04:02:50 2018

@author: bjwil
Assignment #7 - Test Drive
"""
# Test Drive 1 - Chapter 3 - Page 113
# instantiating vowel list to search if letters in string match vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# create an input prompt for the user to enter a string
word = input("Provide a word to search for vowels: ")

# empty dictionary
found = {}

# dictionary keys.  You could create a loop like this... for letter in vowels: found[letter] = 0
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

# check for each letter in the input string if that letter is a vowel in vowels.  If so increase the count in the dictionary for that vowel
for letter in word:
    if letter in vowels:
        found[letter] +=1

# k is the key and v is the value.  print for all keys each value.
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')



# Test Drive 2 - Chapter 3 - Page 131
# instantiating set to search if letters in string match vowels
vowels = set('aeiou')

# create an input prompt for the user to enter a string
word = input("Provide a word to search for vowels: ")       

# find how many of the vowels in vowels intersect with a leter in string.  meaning are the letters in both sets.     
found = vowels.intersection(set(word))

# print all the vowels that were in both sets. does not count how many however.
for vowel in found:
    print(vowel)
