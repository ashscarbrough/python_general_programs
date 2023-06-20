'''
Reverse number
'''
from ast import literal_eval

number = literal_eval(input("Provide an integer to reverse: "))
reverse_number = ""

# for i in range (len(str(number))):
#     reverse_number += str(number%10)
#     number //= 10

while number > 0:
    reverse_number += str(number%10)
    number //= 10

print(reverse_number)
