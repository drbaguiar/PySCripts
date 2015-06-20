# Set range
x = range(20)

# Setup function
def divs_by_2 (num):
    return num % 2 ==0
    
#print filter(divs_by_2,x)
#print map(divs_by_2,x)

print [map(lambda num: num**2, filter(divs_by_2,x))]
print [item**2 for item in x if item %2 ==0]
print [map(lambda num:num**2,filter(lambda num:num %2==0,x))]