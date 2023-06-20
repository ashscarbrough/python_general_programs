'''
Function to reverse string
'''

def reverse_string(string):
    '''
    Function to find reversed string
    Parameters:
        string - (str) string provided by user to reverse
    Return:
        reverse - (str) reversed string
    '''
    reverse = string[:: -1]
    return reverse

user_input = input("Provide a string to reverse: ")

print(reverse_string(str(user_input)))
