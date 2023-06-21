'''
Count Occurrances of number in a string - split/eval
'''
from ast import literal_eval
def main():
    '''
    Main function:
    - Ask User for input: list of integers between 1 and 100
    - Split inputs on white spaces
    - Evaluate each input to integer
    - Make list of unique integers
    - Sort List
    - Provide count for all unique objects
    '''

    user_input = input("Provide a list of integer values: ")
    input_list = user_input.split()
    int_list = [literal_eval(integer) for integer in input_list]

    unique_int_list = []

    for item in int_list:
        if item not in unique_int_list:
            unique_int_list.append(item)

    unique_int_list.sort()

    for int_item in unique_int_list:
        if int_list.count(int_item) == 1:
            print(int_item, "occurred", int_list.count(int_item), "time.")
        else:
            print(int_item, "occurred", int_list.count(int_item), "times.")

if __name__ == "__main__":
    main()
