def evalQuadratic(a, b, c, x):
    return (a*(x**2))+(b*x)+c
   
def square(x):
    return x**2    
      
def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise

    '''
    maxval = min(x,hi)
    ans = max(maxval,lo)
    return ans
    
def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(square(x))

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return [lambda:True, lambda:False][x%2==0]()

def isVowel2(char):
    vowels =vowels = set(['a','e','i','o','u'])
    if char.lower() in vowels:
        return True
    else:
        return False
            
# Test Scripts
print "Quadratic: ", evalQuadratic(3,2,1,2)
print "Square: ", square(3)

lo=2
x = 4
hi = 3
print "Clip: ", clip(lo,x,hi)
print "Fourth Power: ", fourthPower(4)
print "Odd: ", odd(8)
print "Vowel: ",isVowel2("F")