# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import sys
global passes
from sys import exit
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    
    global passes
    
    passes=7
    global secret_number
    
    secret_number=random.randrange(100)
    
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global secret_number
    
    secret_number=random.randrange(100)
    
    global passes
    
    passes=7

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global secret_number
    
    secret_number=random.randrange(1000)

    global passes
    
    passes=10
    
def input_guess(guess):
    # main game logic goes here	
    global passes
    # remove this when you add your code
    guess=int(guess)
    print "Your guess is"+str(guess)
    if passes>1:
        if guess<secret_number:
            passes=passes-1
            print "Higher"
            print "No. of guesses remaining is"+str(passes)
        elif guess>secret_number:
            passes=passes-1
            print "Lower"
            print "No. of guesses remaining is"+str(passes)
        else:
            passes=passes-1
            print "Correct"
            sys.exit()
    elif passes<=1:
            if guess==secret_number:
                print "correct"
                sys.exit()
            else:
                print "You have exhausted your passes+Number is "
        
        

    
# create frame

frame=simplegui.create_frame("Guess the Number",100,200)


# register event handlers for control elements and start frame

inputguess=frame.add_input("Please Enter your number",input_guess,50)
range100=frame.add_button("Range0to100",range100,100)
range1000=frame.add_button("Range0to1000",range1000,100)
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
secret_number = 74	
input_guess("50")
input_guess("75")
input_guess("62")
input_guess("68")
input_guess("71")
input_guess("73")
input_guess("74")