"""
Date Created: 04/23/2020
Name: Yunika Upadhayaya
"""

"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random


def main():
    """
    It generates 10 random number between 0 to 100 and prints those
    to the screen.
    """
    NUM_RANDOM = 10
    MIN_RANDOM = 0
    MAX_RANDOM = 100
    for i in range(NUM_RANDOM):
        rand = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(rand)\



if __name__ == '__main__':
    # This provided line is required at the end of a Python file
    # to call the main() function.
    main()
