# http://www.codeskulptor.org/#user39_0wo2w8bdLq_0.py
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    print "New game. Range is from 0 to",num_range
    print "Number of remaining guesses is",num_guesses
    
# initialize global variables used in your code here
num_range = 100
num_guesses = int(math.ceil(math.log(num_range,2)))
secret_number = random.randint(0, 100)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range, num_guesses, secret_number
    num_range = 100
    num_guesses = int(math.ceil(math.log(num_range,2)))
    secret_number = random.randint(0, 100)
    print
    new_game()
  
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range, num_guesses, secret_number
    num_range = 1000
    num_guesses = int(math.ceil(math.log(num_range,2)))
    secret_number = random.randint(0, 1000)
    print
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global num_range, num_guesses,secret_number
    print
    print "Guess was ", guess
    num_guesses = num_guesses - 1
    print "Number of remaining guesses is",num_guesses
    if int(guess) > secret_number:
        print "Lower!"
    elif int(guess) < secret_number:
        print "Higher!"
    else :
        print "Correct!"
        print
        if num_range == 100:
            range100()
        else:
            range1000()
    if num_guesses == 0:
        print "You lose"
        print
        if num_range == 100:
            range100()
        else:
            range1000() 
        
# create frame
f=simplegui.create_frame("Guess the number: ",200,200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100,200)
f.add_button("Range is [0, 1000)", range1000,200)
f.add_input("Enter a guess", input_guess,200)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric