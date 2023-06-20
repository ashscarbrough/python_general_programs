'''
Evaluate the sum of digits in a number between 0 and 1000
'''
from ast import literal_eval

number = literal_eval(input("Enter a number between 0 and 1000: "))

numbersum = number % 10
number //= 10
numbersum += number % 10
number //= 10
numbersum += number % 10

print("The sum of digits in the number is:", numbersum)
