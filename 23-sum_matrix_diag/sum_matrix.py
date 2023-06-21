'''
Function to find the sum of the diagonal of a matrix
'''

MATRIX_SIZE = 4

def sum_of_matrix_major_diagonal(matrix):
    '''
    Find the sum of the major diagonal of a matrix
    '''
    sum = 0

    for num in range(0, len(matrix[0])):
        sum += matrix[num][num]

    return sum


if __name__ == "__main__":
    matrix = []
    matrix.append([1, 2, 3, 4])
    matrix.append([5, 6, 7, 8])
    matrix.append([9, 10, 11, 12])
    matrix.append([13, 14, 15, 16])
    # for row in MATRIX_SIZE:
    #     user_input= input("Provide a list of 4 numbers for matrix row: ")
    #     matrix.append[]

    print("sum =", sum_of_matrix_major_diagonal(matrix))
