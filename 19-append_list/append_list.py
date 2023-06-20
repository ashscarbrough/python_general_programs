'''
A function to create a list of 1000 random numbers and return the total count of the list
'''
import random

def random_list_generator(random_list):
    '''
    function to append 1000 numbers between 0 and 9 inclusive into a list
    Parameter:
        random_list = empty list
    '''
    for i in range(1000):
        random_list.append(random.randint(0,9))

def main():
    '''
    Main function to initialize and print the count of each number in the list
    '''
    rand_list = []
    random_list_generator(rand_list)

    for i in range(10):
        print("You have", rand_list.count(i), "of number", i, "in your list!")

main()
