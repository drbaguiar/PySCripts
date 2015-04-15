# Programming background in Python.

# The first exercise allows you to assess your ability to program in Python.
# As a data analyst, you will spend much of your time writing code and
# programs to work with data or to build mathematical, statistical, or
# machine learning models to find insights from data.

# Complete this function that modifies a list of integers.
# 1)  For numbers that are multiples of three replace the integer with the string "Fizz".
# 2)  For numbers that are multiples of five replace the integer with the string "Buzz".
# 3)  For numbers that are multiples of both three AND five replace the integer
    # with the string "FizzBuzz"

# Your function should take in a list of integers as input.
# Your function should not modify the input list.
# Your function should return an updated list with integers and strings.

def fizzbuzz(num_range):
	fizzbuzzString = []
    for each in num_range:
        if each % 3 == 0 and each % 5 == 0:
			fizzbuzzString += "fizzbuzz" + " "
        elif each % 3 == 0:
            fizzbuzzString += "fizz" + " "
        elif each % 5 == 0:
            fizzbuzzString += "buzz" + " "
        else:
            fizzbuzzString += each + " "
	return fizzbuzzString (:-1)