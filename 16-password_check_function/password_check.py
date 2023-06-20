'''
Create function that checks for a password requirements are matched.
Requirements:
    - Password of MIN_LENGTH (8)
    - Alpha-numeric
    - 2 digits
'''

MINIMUM_PASSWORD_LENGTH = 8

def check_password_length(password):
    '''
    Function checks that password length is greater than the minimum allowable
    Parameters:
        password - (str) user provided password
    Return:
        True/False - (bool) password is minimum length allowed
    '''
    return True if len(password) >= MINIMUM_PASSWORD_LENGTH else False

def check_password_alphanumeric(password):
    '''
    Function checks that password is alpha numeric
    Parameters:
        password - (str) user provided password
    Return:
        True/False - (bool) password is alphanumeric
    '''
    return password.isalnum()

def check_password_two_digits(password):
    '''
    Function checks that password has at least two digits
    Parameters:
        password - (str) user provided password
    Return:
        True/False - (bool) password has minimum digit amount
    '''
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1

    return True if digit_count >= 2 else False

def main():
    '''
    Main function - Gets user password and determines if it is valid
    '''
    password = input("Provide a password: ")

    if check_password_length(password) and check_password_alphanumeric(password) \
        and check_password_two_digits(password):
        print("Password is valid!")
    else:
        print("Password is invalid!")

main()
