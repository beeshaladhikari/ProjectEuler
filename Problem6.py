#Problem 6: Sum square difference

#
#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and #the square of the sum.
#

numbers = range(1,101)

def sumOfSquares(number):
	Sum = 0
	for num in number:
		Sum += (num**2)
	return Sum	


def squareOfSum(number):
	Sum = 0
	sqSum = 0
	for num in number:
		Sum += num
		sqSum = (Sum**2)
	return sqSum
	
print(sumOfSquares(numbers))
print(squareOfSum(numbers))

difference = squareOfSum(numbers) - sumOfSquares(numbers)
print(difference)
