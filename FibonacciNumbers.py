
#Turn the following English description into code:

#Create a list with two numbers, 0 and 1, respectively.
#For 40 times, add to the end of the list the sum of the last two numbers.
#What is the last number in the list?
#To test your code, if you repeat 10 times, rather than 40, your answer should be 89.


x = 0
y = 1
for i in range(40):
    x, y = y, x + y
    print i+1,y