'''
application to create and print matix binary
'''
from ast import literal_eval

def head_or_tail(value):
    '''
    Function to create value of head or tail
    Input: value - (int) binary value
    Output: char - (str) H or T based on binary value
    '''
    return "H" if value == "0" else "T"

def print_matrix(matrix):
    '''
    Function to Print Matrix
    Input: matrix - list(list())
    Output: None
    '''

    line = ""
    for row in range(3):
        for column in range(3):
            line += head_or_tail(matrix[row][column]) + " "
        print(line)
        line = ""

def full_binary(binary_num):
    '''
    Function to create a full binary string to represent number
    Input: binary_num - (str) binary representation of number
    Output: binary_num - (str) expand binary to fit grid
    '''
    print(type(binary_num))
    while len(binary_num) != 9:
        binary_num = "0" + binary_num
    return binary_num

def main():
    '''
    Main function to get user input as in between 0-511.
    Convert number to binary, expand it
    Place binary number in matrix and print it
    Input: None
    Output: None
    '''

    user_number = literal_eval(input("Provide a number between 0 and 511: "))

    binary = bin(user_number)[2:]
    binary = full_binary(binary)
    matrix = []

    for row in range(3):
        matrix.append([])
        for column in range(3):
            matrix[row].append(binary[(row * 3) + column])
        print(matrix[row])

    print_matrix(matrix)

if __name__ == "__main__":
    main()
