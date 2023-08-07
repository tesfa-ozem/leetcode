
'''
Function to get the factorial of a number
'''
def factorial(n:int)->int:
	if n == 0:
		return 1

	return n * factorial(n-1);

value = factorial(5)

print(value)