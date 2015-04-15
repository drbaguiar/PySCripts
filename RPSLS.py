# Rock-paper-scissors-lizard-Spock 
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
    if name in ("Scissors", "scissors"):
        number = 4
    elif name in ('Spock', "spock"):
        number = 1
    elif name in ('Paper', 'paper'):
        number = 2
    elif name in ('Lizard', 'lizard'):
        number = 3
    elif name in ('Rock', 'rock'):
        number = 0
    else: 
        print "Please make a valid choice"
        number = 99
    return number

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 4:
        name = "scissors"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 0:
        name = "rock"
    else: 
        name  = "Please make a new choice"
    return name

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
   
    
    # print a blank line to separate consecutive games
    print
    
    # print out the message for the player's choice
    print "Player chooses", player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choice
    
    # compute difference of comp_number and player_number modulo five
    diff = comp_number - player_number % 5
  
  # use if/elif/else to determine winner, print winner message
    if diff == 0:
        print "Player and computer tie!"
    elif diff < 0:
        print "Player wins!" 
    else:
        print "Computer wins!"
        
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
#player_choice = raw_input("Please input your choice (rock, paper, scissors, lizard, or Spock): ")
#rpsls(player_choice)

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

