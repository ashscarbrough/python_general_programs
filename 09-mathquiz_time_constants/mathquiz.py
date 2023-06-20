'''
Math Quiz to time and assess questions and answers
'''

from ast import literal_eval
import random
import time

correct_count = 0  # Number of correctly answered quiz problems
count = 0  # Count the number of questions
NUMBER_QUIZ_QUESTIONS = 10  # Constant

start_time = time.time()

while count < NUMBER_QUIZ_QUESTIONS:
    # Generate two random numbers
    rand_num1 = random.randint(0, 50)
    rand_num2 = random.randint(0, 50)

    user_answer = literal_eval(input("What is " + str(rand_num1) + " + " + str(rand_num2) + "? "))

    answer = rand_num1 + rand_num2

    if user_answer == answer:
        correct_count += 1
        print("Correct!")
    else:
        print("Incorrect!", rand_num1, "+", rand_num2, "=", answer)

    count += 1

end_time = time.time()

print("You scored", correct_count, "out of", NUMBER_QUIZ_QUESTIONS)
print("Quiz time:", round((end_time - start_time), 2), "seconds")
