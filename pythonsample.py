nums = []
i = 0

while i < 3:
	tmp = int(input("Enter a number: "))
	nums.append(tmp)
	i = i + 1
	
print "Numbers as entered are: ",nums
nums.sort()

print "Numbers sorted are: ",nums
