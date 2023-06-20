'''
A function that will find the number of times a substring is found in a string
'''

def find_substring(substring, string):
    '''
    Function to count the number of times a substring shows up.
    Parameters:
        - substring - (str) user provided substring to search for in the larger string
        - string - (str) user provided string
    Returns:
        - count - (int) the number of times the substring was found
    '''
    count = string.count(substring)
    return count

def main():
    '''
    main function to get user string and substring and print the resulting count found
    '''
    user_string = input("Provide a string to search: ")
    user_substring = input("Provide a substring to search for: ")

    print("Your substring was found", find_substring(user_substring, user_string), "times!")

main()
