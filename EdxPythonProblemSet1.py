#s = 'sjoaiucqfryabef'
s = "azcbobobegghakl"


# Count vowels in string
vowels =vowels = set(['a','e','i','o','u'])
count = 0
for character in s:
    if character in vowels:
        count = count+1
print "Number of vowels:",  count

#Count bob in string
import re
count = len(re.findall("(?=bob)", s))
print "Number of times bob occurs is: ",count

# Find the longest continsubstring in alphabetical order
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest