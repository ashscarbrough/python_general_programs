'''
Sort and Display set of sorted numbers
'''
number_list = [1002, 15, 66, 64, 202, 568]
number_list.sort()
print(number_list)


# Native sort with predetermined list of 3 elements
native_number_list = [62, 88, 23]

if native_number_list[0] > native_number_list[1]:
    native_number_list[0], native_number_list[1] = native_number_list[1], native_number_list[0]

if native_number_list[0] > native_number_list[2]:
    native_number_list[0], native_number_list[2] = native_number_list[2], native_number_list[0]

if native_number_list[1] > native_number_list[2]:
    native_number_list[1], native_number_list[2] = native_number_list[2], native_number_list[1]

print(native_number_list)
