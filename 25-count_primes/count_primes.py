'''
Example function to find prime list and count them
'''

def count_primes(num):
    '''
    Function to find list of primes
    '''

    if num < 2:
        return 0

    prime_list = [2]
    num_range = 3

    while num_range <= num:
        for prime in prime_list:  # for y in range(3, num_range, 2):
            if num_range % prime == 0:
                num_range += 2
                break
        else:
            prime_list.append(num_range)
            num_range += 2

    print(prime_list)
    return len(prime_list)

print(count_primes(100))
