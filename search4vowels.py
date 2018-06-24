# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 10:44:18 2018

@author: bjwil
"""

from collections import Counter
from PyDictionary import PyDictionary
import string
from timeit import timeit
from itertools import count


# function to search for vowels of a word
def search4vowels(word:str) ->set:
    '''Display any vowels found in a supplied word.  I added a count function
    that I had just learned as well from collections'''
    # initialize dictionary to input letters from vowels and counts
    dlist = {}
    # set word to lowercase
    word = word.lower()
    # initialize vowels as a set
    vowels = set('aeiou')
    # found will equal all the letters in the word that are in the set of vowels.  Will only include letters in vowels since it's
    # the first argument
    found = vowels.intersection(set(word))
    # print out all the vowels in found that were intersected with the word
    '''for vowel in found:
        print(vowel)'''
    # append the dictionary for each letter in vowel
    for letter in vowels:
        # count how many times each vowel is in the word
        c = word.count(letter)
        # add the key[letter] and it value at same time
        dlist[letter] = c 
    # coerece dictionary to Counter
    counter = Counter(dlist)
    
    # return all the letters in found which are all the vowels in the word, the Counter(), and the amount of the most common vowel
    return found, counter, counter.most_common(1)[0][1]

# test twice
print(search4vowels('python is great'))
print(search4vowels('wordsWithMoreThanOne+CASE'))
# time 10,000 loops.  prints alot of text
'''if __name__=='__main__':
    from timeit import Timer
    t = Timer(lambda: search4vowels('python is great'))
    print(t.timeit(number=10000))'''

# speed up function by not looping and printing and initalizing found variable
def search4vowels_withoutFound(word:str) -> set:
    '''Display any vowels found in a supplied word.  I added a count function
    that I had just learned as well from collections'''
    # initialize dictionary to input letters from vowels and counts
    dlist = {}
    # set word to lowercase
    word = word.lower()
    # initialize vowels as a set
    vowels = set('aeiou')
    # append the dictionary for each letter in vowel
    for letter in vowels:
        c = word.count(letter)
        dlist[letter] = c    
    counter = Counter(dlist)
    
    # return all the vowels which intersect word, the Counter(), and the most common vowel AND amount this time
    return vowels.intersection(set(word)), counter, counter.most_common(1)[0]

# test twice
print(search4vowels_withoutFound('python is great'))
print(search4vowels_withoutFound('wordsWithMoreThanOne+CASE'))
# time 10,000 loops
if __name__=='__main__':
    from timeit import Timer
    t = Timer(lambda: search4vowels_withoutFound('python is great'))
    print(t.timeit(number=10000))
   
# function which includes letters to search for.    
def search4letters(phrase:str, letters = 'aeiou') -> set:
    '''Display any letters entered that are found in a supplied phrase.  I added a count functionality
    that I had just learned as well from collections and definitions method for fun'''
    # initialize a translator from string. datatype is a dictionary where punctuation is give value of none.
    # see acsii table for python at https://www.dotnetperls.com/ascii-table-python
    translator = str.maketrans('', '', string.punctuation)
    # takes all the punctuation inside a phrase out of the phrase with translate function
    phrase = phrase.translate(translator)
    # splits all the words up in the phrase
    defineSeperateWords = phrase.split()
    # creates a python dictionary
    dictionary = PyDictionary(defineSeperateWords)
    # add to definition library
    library = {}
    # initialize dictionary to input letters from vowels and counts
    dlist = {}
    # append the dictionary for each letter in vowel
    for letter in letters:
        c = phrase.count(letter)
        dlist[letter] = c    
    counter = Counter(dlist)
    # prints each meaning if meaning is found through 'lxml' or 'html' parsing from BeautifulSoup calling of PyDictionary module
    for word in dictionary:
        try:
            # print(PyDictionary(word).getMeanings())
            library[word] =  PyDictionary(word).getMeanings()[word] 
        # not sure about this and why the function 'PyDictionary(word).printMeanings()' in core.py gives this error
        # line 27 in printMeansings for k in dic[key].keys():
        # also need the Attribute error for getMeanings()
        except AttributeError:
            print("Word not found in python dictionary.")
        
    # return all the letters which intersect the phrase, the Counter(), and the most common vowel AND amount this time
    return set(letters).intersection(set(phrase)), counter

# test three times
search4letters('galaxy', 'xyz')
print(search4letters(letters = 'xyz', phrase = 'galaxy'))
search4letters('life, the universe, and everything', 'aeiou')
# two more tests.  has a lot of text to test so many times
'''
search4letters('supercalifragilisticexpialidocious', 'aeiou')
search4letters('Youth is wasted on the young', 'you')
'''
phrase = 'Youth is wasted on the young'
letters = 'you'
# time 10 loops. lot of text
'''if __name__=='__main__':
    from timeit import Timer
    t = Timer(lambda: search4letters('Youth is wasted on the young', 'you'))
    print(t.timeit(number=10))'''


def test(f):
    data = "sunset."
    for _ in range(5):
        f(data)
        data = data + data

def speed_compare():
    results = {
        'search4vowels': timeit(
            'test(search4vowels)',
            setup='from __main__ import (test, search4vowels)',
            number=1000,
        ),
        'search4vowels_withoutFound': timeit(
            'test(search4vowels_withoutFound)',
            setup='from __main__ import (test, search4vowels_withoutFound)',
            number=1000,
        ),
        'search4letters': timeit(
            'test(search4letters)',
            setup=(
                'from __main__ import (test, search4letters)\n'
                'from itertools import count\n'
                'from string import ascii_lowercase\n'
            ),
            number=1,
        )
    }
    for k, v in results.items():
        print(k, 'scored', v)