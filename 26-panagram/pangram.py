'''
check if string is a pangram (contains all letters in the alphabet)
'''

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create set of alphabet
    alphabetset = set(alphabet)

    # Remove all spaces
    str1 = str1.replace(" ", "")

    # Convert string to lowercase
    str1 = str1.lower()

    # Convert string to set
    str1 = set(str1)

    return str == alphabetset

ispangram("The quick brown fox jumps over the lazy dog")
