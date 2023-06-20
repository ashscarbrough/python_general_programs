'''
Test Random
'''

from ast import literal_eval
import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)
number3 = random.randint(0,9)

answer = literal_eval(input("What is " + str(number1) + " + "\
    + str(number2) + " + " + str(number3) + "? "))

print(number1, "+", number2, "+", number3, "=", \
    (number1 + number2 + number3))
print("Your answer is: ", number1, "+", number2, \
    "+", number3, "=", answer)

if answer == (number1 + number2 + number3):
    print("Correct")
else:
    print("Incorrect")
