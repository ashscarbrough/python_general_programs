'''
Reverse number with error checking
'''
from ast import literal_eval

number = literal_eval(input("Provide an integer to reverse: "))
reverse_number = ""

try:
    for i in range (len(str(number))):
        reverse_number += str(number%10)
        number //= 10
except:  # TypeError
    print("Not an integer")
finally:
    print(reverse_number)
