high = 100 #high end of guess - cut as needed
low = 0 # low end of guess - cut as needed
numGuesses = 0

print 'Please think of a number between 0 and 100!'

while True:
    guess = (high + low)/2
    print "Is your secret number " + str(guess) + "?"
    user = raw_input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I  guessed correctly. ")
    if user == 'h':
        high = guess
        numGuesses +=1
    elif user == 'l':
        low = guess
        numGuesses +=1
    elif user == 'c':
        numGuesses +=1
        break
    else:
        print "Sorry, I did not understand your input."
        
print "Game over. Your secret number was: " + str(guess)
#print "I got it in " + str(numGuesses) + " guesses!"