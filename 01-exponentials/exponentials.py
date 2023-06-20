'''
Display 1st, 2nd, and 3rd exponents of a list of numbers
'''

def exponent(n):
    '''
    Exponent function, print first, second, and third power
    '''
    print(n, "\t", n**2, "\t", n**3)

print("a \t a^2 \t a^3")

numlist = [1, 2, 3, 4]

for i in numlist:
    exponent(i)
    