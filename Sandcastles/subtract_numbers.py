"""
Date Created: 04/23/2020
Name: Yunika Upadhayaya
"""

"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    It prompts user to enter two numbers and prints its sum.
    """
    print("This program subtracts one number from another.")
    first_number = input("Enter first number: ")
    second_number = input("Enter second number: ")

    result = float(first_number) - float(second_number)
    print("The result is",result)


if __name__ == '__main__':
    """
    This provide line calls and runs the main function 
    """
    main()
