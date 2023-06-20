'''
Create Fizz Buzz type solution for numbers 100 to 200:
- if number is divisible by 5 add number to a list to print
- if number is divisible by 5 and six, skip it
- if number is divisible by 6 add the number to the list to print
- print only 10 numbers per line
'''

number_string = ""
count = 0

for num in range (100, 200+1):
    if num % 5 == 0:
        if num % 6 != 0:
            number_string += " " + str(num)
            count += 1
    elif num % 6 == 0:
        number_string += " " + str(num)
        count += 1

    if count > 9:
        number_string += "\n"
        count = 0

print(number_string)
