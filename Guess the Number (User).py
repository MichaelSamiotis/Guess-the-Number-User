#!/usr/bin/env python
# coding: utf-8

# In[1]:


def guessing_game(x):
    #importing the random package so we can call the random.randint function
    import random

    #Defining the lower and upper limit for the range of the guessing game
    min_limit = 1
    max_limit = x
    feedback = 0

    #Creating a loop so the computer guesses a number between the limits
    while feedback != 'C':
        
        if min_limit != max_limit: 
        #I could add this in the while statement as 'and min_limit != max_limit'.
        #The issue that would arise with that is that, it could be possible that
        #the min_limit being equal to the max_limit from the first guess
        #which would exit the loop immediately without allowing the user to confirm it
        
            #Guessing of the number from the computer
            guess = random.randint(min_limit,max_limit)
        
        else:
            guess = max_limit #or guess = min_limit as at that point min_limit = max_limit 
            
        #Creating a feedback provided by the user and redefining the new limits
        feedback=input(f'If {guess} is higher than your number, type \'H\', \
if it\'s lower type \'L\' or type \'C\' if it\'s correct. ')
            
        if feedback == 'L':
            min_limit = guess+1
        elif feedback == 'H':
            max_limit = guess-1

    #Creating the final message when the number is being guessed correctly by the computer
    print(f'Congrats, the computer has guessed your number correctly! The secret number is {guess}.')

guessing_game(100)

