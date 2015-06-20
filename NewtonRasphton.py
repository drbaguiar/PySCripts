x = 12345
epsilon = 0.01
ans = x/2.0
numGuesses = 0

while abs(ans*ans-x) >= epsilon:
    numGuesses += 1
    ans = ans -(((ans**2)-x)/(2*ans))

print "Number of Gussess: " + str(numGuesses)
print str(ans) + " is close to square root of " + str(x)