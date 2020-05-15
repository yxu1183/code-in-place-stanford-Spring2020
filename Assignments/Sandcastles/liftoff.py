"""
Date Created: 04/23/2020
Name: Yunika Upadhayaya
"""

"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    """
    It prints the number from 10 to 1 backwards. At, 0
    it prints Liftoff.
    """
    for i in range(10, 0, -1):
        print(i)
    print("Liftoff!")


if __name__ == "__main__":
    # This provided line is required at the end of a Python file
    # to call the main() function.
    main()
