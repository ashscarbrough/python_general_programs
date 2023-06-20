'''
Generate a Lottery 
'''
from ast import literal_eval
import random

# Generate a Lottery Number
lotterygen = random.randint(0, 999)
lottery = lotterygen

# Prompt user to enter a guess
guessgen = literal_eval(input("Provide your lottery guess as a three digit number: "))
guess = guessgen

# Get digits from lottery number
lotterydigit3 = lottery % 10
lottery //= 10
lotterydigit2 = lottery % 10
lottery //= 10
lotterydigit1 = lottery % 10

# Get digits from guess number
guessdigit3 = guess % 10
guess //= 10
guessdigit2 = guess % 10
guess //= 10
guessdigit1 = guess % 10

print("The lottery number is:", lotterygen)

# Check guess:
# Exact match
if guessgen == lotterygen:
    print("Exact Match: You win $10,000!")
# Match all numbers out of order
elif ((guessdigit1 == lotterydigit1 and guessdigit2 == lotterydigit3 \
    and guessdigit3 == lotterydigit2) or (guessdigit1 == lotterydigit3 and \
        guessdigit2 == lotterydigit2 and guessdigit3 == lotterydigit1) or \
            (guessdigit1 == lotterydigit2 and guessdigit2 == lotterydigit1 \
                and guessdigit3 == lotterydigit3) or (guessdigit1 == lotterydigit2 \
                    and guessdigit2 == lotterydigit3 and guessdigit3 == lotterydigit1) \
                        or (guessdigit1 == lotterydigit3 and guessdigit2 == lotterydigit1 \
                            and guessdigit3 == lotterydigit2)):
    print("All digits match, you win $3,000!")
elif ((guessdigit1 == lotterydigit1) or \
    (guessdigit1 == lotterydigit2) or \
        (guessdigit1 == lotterydigit3) or \
            (guessdigit2 == lotterydigit1) or \
                (guessdigit2 == lotterydigit2) or \
                    (guessdigit2 == lotterydigit3) or \
                        (guessdigit3 == lotterydigit1) or \
                            (guessdigit3 == lotterydigit2) or \
                                (guessdigit3 == lotterydigit3)):
    print("Match one digit: You win $1,000!")
else:
    print("Sorry, you did not win.")
