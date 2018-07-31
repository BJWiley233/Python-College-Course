# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 18:50:50 2018

@author: bjwil
"""
import os
os.chdir("C:\\Users\\bjwil\\Python College Course")
os.getcwd()
todos = open('todos.txt', 'a')

print('Put out the trash.', file = todos)
print('Feed the cat.', file = todos)
print('Prepare tax return.', file = todos)

todos.close()

with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end = '')

with open('vsearch.log') as log:
    test = log.readlines()
