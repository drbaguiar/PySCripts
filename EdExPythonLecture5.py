def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 0
    count = 1
    if exp == 1:
        return base
    elif exp == 0:
        return 1

    while exp > 1:
        if count ==1 :
            result = base * base
            count += 1
        else:
            result *=base
        exp-=1
    return result
        
def recurMul(a,b):
    if b==1:
        return a
    else:
        return a+ recurMul(a,b-1)

def factR(n):
    if n==1:
        return n
    else:
        return n * factR(n-1)    

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp==0:
        return 1
    else:
        return base * recurPower(base,exp-1)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp==0:
        return 1
    elif exp%%2 ==0:
        return base * recurPower(base,exp/2)
    else:
        return 1