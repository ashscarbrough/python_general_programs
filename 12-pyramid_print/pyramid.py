'''
Print a triangle based on the number of lines provided by the user
'''

from ast import literal_eval

user_number = literal_eval(input("How many lines should comprise our star pyramid? "))

if 1 <= user_number < 15:
    baseline = str(user_number)

    # Get the total length of the baseline
    # Concatinate string for user number to 1
    for num in range(user_number - 1, 0, -1):
        baseline += " " + str(num)

    for num in range(2, user_number + 1):
        baseline += " " + str(num)

    # print whole pyramid
    for mainNum in range(1, user_number + 1):
        line = str(mainNum)  # Initialize a string for our level
        for num in range(mainNum - 1, 0, -1):  # Obtain first half of level
            line += " " + str(num)
        for num in range(2, mainNum + 1):
            line += " " + str(num)
        print(line.center(len(baseline)))

# user_number = literal_eval(input("How many lines should comprise our star pyramid? "))

# if 1 <= user_number < 15:
#     baseline = str(user_number)

#     # Get the total length of the baseline
#     # Concatinate string for user number to 1
#     for num in range(user_number - 1, 0, -1):
#         baseline += " *"

#     for num in range(2, user_number + 1):
#         baseline += " *"

#     # print whole pyramid
#     for mainNum in range(1, user_number + 1):
#         line = "*"  # Initialize a string for our level
#         for num in range(mainNum - 1, 0, -1):  # Obtain first half of level
#             line += " *"
#         for num in range(2, mainNum + 1):
#             line += " *"
#         print(line.center(len(baseline)))
        