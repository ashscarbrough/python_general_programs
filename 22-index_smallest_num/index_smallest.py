'''
Function to find the index of the smallest number in list
'''
from ast import literal_eval

def index_of_smallest_number(num_list):
    '''
    Function to get the index of the first occurance of smallest number in a list
    '''
    smallest_number = min(num_list)
    return num_list.index(smallest_number)

user_list = input("Enter a list of numbers: ")
split_inputs = user_list.split(",")
number_list = [literal_eval(num) for num in split_inputs]

print("The index of the first occurance of the smallest number is:",
      index_of_smallest_number(number_list))
