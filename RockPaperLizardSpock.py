# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
        
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        number = -1
    return number


def number_to_name(number):
    
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        name = "invalid"    
    return name
 
    

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice
    print "Player chooses" , player_choice

    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses" , comp_choice

    # compute difference of comp_number and player_number modulo five
    if ( comp_number >= 0 and player_number >= 0 ):
        difference = (comp_number - player_number) % 5
    else:
        difference = -1

    # use if/elif/else to determine winner, print winner message
    if (difference == 1 or difference == 2):
        print "Computer Wins!"
    elif (difference == 3 or difference == 4):
        print "Player Wins!"    
    elif (difference == 0):    
        print "Player and computer tie!"
    else:
        print "Invalid Input"    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
#rpsls("test_invalid_input")

# always remember to check your completed program against the grading rubric



