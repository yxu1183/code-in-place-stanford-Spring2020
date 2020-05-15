"""
Date Created: 04/18/2020
Name: Yunika Upadhayaya
"""
from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
StoneMasonKarel should solves the "repair the quad" problem 
from Assignment 1. Program works for all of the 
sample worlds supplied in the starter folder.
"""


def move_4rows():
    for i in range(4):
        move()


def turn_around():
    """
    This function turns the beeper around.
    """
    turn_left()
    turn_left()


def check_put_beeper():
    """
    This function moves along the column, checks whether it contains the beeper,
    puts the beeper if it does not contain one and comes back.
    """
    turn_left()
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
            move()
    if front_is_blocked():
        if no_beepers_present():
            put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def main():
    """
    Implements all the function to print the desired output in karel space.
    """
    for i in range(3):
        check_put_beeper()
        move_4rows()
    check_put_beeper()


if __name__ == "__main__":
    """
    This if statement opens up the karel space when calling main().
    """
    run_karel_program()
