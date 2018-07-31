# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:32:48 2018

@author: bjwil
"""
import os

os.chdir('C:\\Users\\bjwil\\Python College Course')

name = input("What would you like me to name your file as? Do NOT include the extension .txt or any other extension! ")
name = name + '.txt'
text = list('Hello World This is your conscience talking Now is the time to relax and reminiscence'.split())
with open(name, 'a') as file_:
    for word in text:
        print(word, file = file_, end = '\n')
print('Closing ... ' + name)
print("===========================")
print('Opening ... ' + name)
newText = input('What sentence should I add to the last line of the file? ')
newText = list(newText.split())
with open(name, 'a') as file_:
    for word in newText:
        print(word, file = file_, end = '\n')
print('Closing ... ' + name)
print("===========================")
print('Opening ... ' + name)
with open(name, 'r') as file_:
    alist = [line.rstrip() for line in file_]
    for word in alist:
        print(word)
        

 