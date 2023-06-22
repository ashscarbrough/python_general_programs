'''
Function to print star pyramid
'''
from ast import literal_eval

rows = literal_eval(input("How many lines do you want the pyramid? "))

for x in range (rows):
    print(' ' * (rows - x - 1) + "*" * (2 * x + 1))
