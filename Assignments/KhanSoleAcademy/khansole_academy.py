"""
Date Created: 04/23/2020
Name: Yunika Upadhayaya
"""

"""
File: khansole_academy.py
-------------------------
This program will randomly generate simple addition problems 
for the use, reads in the answer from the user, and then checks
to see if they got it right or wrong, until the user appears to 
have mastered the material.
"""

import random


def main():
    counter = 0

    # Run the loop only till the user correctly answers 3 sums in a row
    while counter < 3:
        random_min = 10
        random_max = 99
        # Generate two random variables from 10 to 99 (inclusive)
        first_rand = random.randint(random_min, random_max)
        second_rand = random.randint(random_min, random_max)

        # Ask for user input
        print("What is", first_rand, " +", second_rand, "?")
        print("Your answer: ", end='')
        answer = int(input())

        sum = first_rand + second_rand

        # Check if the answer is correct to sum
        if sum != answer:
            print("Incorrect. The expected answer is ", sum)
            counter = 0
            # Reset the counter to 0 if the sum is incorrect
        else:
            # Increase the counter if the sum is correct
            counter = counter + 1
            if counter == 1:
                print("Correct! You've gotten 1 correct in a row.")
            elif counter == 2:
                print("Correct! You've gotten 2 correct in a row.")
            elif counter >= 3:
                print("Correct! You've gotten 3 correct in a row.")
                print("Congratulations! You mastered addition.")


if __name__ == '__main__':
    # This provided line is required at the end of a Python file
    # to call the main() function.
    main()
