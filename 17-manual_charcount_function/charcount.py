'''
Function to search for the number of a particular character in a string
'''

def char_count(user_char, user_string):
    '''
    Function counts the numbers of a particular character in a string
    Parameters:
        - user_char - (str) single character provided by user to count
        - user_string - (str) user privded string to search
    Return:
        - count - (int) number of times the character was found in string
    '''
    count = 0
    for char in user_string:
        if user_char == char:
            count += 1

    return count

def main():
    '''
    Main function to ask user char and string and begin count process
    '''

    user_string_input = input("Provide a string to search: ")
    user_char_input = input("Provide a character you want a count for in the string: ")

    print("There are", char_count(user_char_input, user_string_input), "in the string!")

main()
