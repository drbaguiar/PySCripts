x = 25
epsilon = 0.01
low = 0.0
high = x
numGuesses = 0
ans = (high+low)/2.0

while abs(ans**2-x) >= epsilon:
    print "Low: "+ str(low) + " High: "+ str(high) + " Ans: "+str(ans)
    numGuesses += 1
    if ans**2 <x:
        low = ans
    else:
        high=ans
    ans= (high+low)/2.0

print "Number of Gussess: " + str(numGuesses)
print str(ans) + " is close to square root of " + str(x)