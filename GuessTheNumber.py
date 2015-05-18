# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

max_range = 100

# helper function to start and restart the game
def new_game():
    # global variables used in the code 
    global secret_number
    global max_range
    global max_guesses
    
    if (max_range == 100):
        max_guesses = 7
    elif (max_range == 1000):
        max_guesses = 10
        
    secret_number = random.randrange(0, max_range)
    print "\nNew Game, Range is from 0 to" , max_range 
    print "Number of remaning guesses is", max_guesses


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global max_range
    max_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global max_range
    max_range = 1000
    new_game()
   
    
def input_guess(guess):
    
    # check whether the input is an integer, 
    # if not, throw an exception
    try:
        user_guess = int(guess)
    except ValueError, Argument:
        print "\nInvalid guess. Only an integer guess is valid\n", Argument
        return    
   
    print "\nGuess was" , user_guess        
    # decrement the guesses
    global max_guesses
    max_guesses = max_guesses - 1
    print "Number of remaning guesses is", max_guesses

    # if the remaining guesses are 0, start a new game 
    if (max_guesses == 0):
         if (user_guess == secret_number):
            print "Correct!"
            new_game()
         else:   
            print "You ran out of guesses, the number was", secret_number
            new_game() 
    else:    
        # guide the player for the next guess
        if (user_guess == secret_number):
            print "Correct!"
            new_game()
        elif (user_guess > secret_number): 
            print "Lower!"
        elif (user_guess < secret_number):  
            print "Higher!"        


    
# create frame
frame = simplegui.create_frame("Guess the Number game", 400, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100]", range100, 200)
frame.add_button("Range is [0,1000]", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)


# call new_game 
new_game()


