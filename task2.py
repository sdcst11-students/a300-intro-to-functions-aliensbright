"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random
guess=0
num=random.randint(0,100)

def title():
    print('These are the rules for the game. You will need to guess a number.\nEnter a number from 0-100 and I will tell you if it is too low or high.')
title()
def game():
    guess=int(input('Enter a number from 0-100:'))
    if guess<num:
        print('Too Low.')
    elif guess>num:
        print('Too High.')
    elif guess==num:
        print('You got it right')
        exit()
for i in range(10):
    game()
else:
    print(f'You failed. The missing number was {num}.')