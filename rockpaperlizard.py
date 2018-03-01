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
    # delete the following pass statement and fill in your code below
    

    # convert name to number using if/elif/else
    # don't forget to return the result!
    
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    
    

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number=="0":
        return "rock"
    elif number=="1":
        return "Spock"
    elif number=="2":
        return "paper"
    elif number=="3":
        return "lizard"
    elif number=="4":
        return "scissors"
  
        
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
player_choice=raw_input("Please Enter your choice")
def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    
    # print a blank line to separate consecutive games
    print (" ") 
    # print out the message for the player's choice"
    
    print "player choice is "+player_choice
    
    

    # convert the player's choice to player_number using the function name_to_number()
    
    player_number=name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    
    comp_number=random.randrange(4)
    
    

    # convert comp_number to comp_choice using the function number_to_name()
    
    comp_choice=number_to_name(str(comp_number))
    
    # print out the message for computer's choice
    
    print "Computer choice is "+str(comp_choice)

    # compute difference of comp_number and player_number modulo five
    
    dif=(comp_number-player_number)%5
    
    # use if/elif/else to determine winner, print winner message
    if dif==0:
        print "It is a tie"
    elif dif>2:
        print "Player Wins"
    elif dif<=2:
        print "Computer Wins"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls(player_choice)
player_choice=raw_input("Please Enter your choice")
rpsls(player_choice)


# always remember to check your completed program against the grading rubric

