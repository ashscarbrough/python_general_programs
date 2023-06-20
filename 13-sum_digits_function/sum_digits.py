'''
Function to count the sum of digits in a number
'''

from ast import literal_eval

def sum_digits(num):
    '''
    Method to count the number of digits in a number
    Parameters
        - num: number provided by user
    Outputs
        - sum of all digits comprising number
    '''
    num_sum = 0
    while num > 0:
        num_sum += (num % 10)
        num //= 10
    return num_sum

user_number = literal_eval(input("Provide a number that you want a sum for all the digits: "))
print("The sum of your number is: ", (sum_digits(user_number)))
