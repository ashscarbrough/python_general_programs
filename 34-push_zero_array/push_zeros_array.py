'''
Move Zeros to back of array in place
'''

array = [0, 9, 21, 44, 0, 12, 4, 62, 0, 1]

array2 = []

zero_count = 0

for position, value in enumerate(array):
    if value != 0:
        array2.append(value)
    else:
        zero_count += 1

for i in range(zero_count):
    array2.append(0)

print(array)
print(array2)
