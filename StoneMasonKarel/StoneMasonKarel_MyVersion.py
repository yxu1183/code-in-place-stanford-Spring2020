"""
Date Created: 04/18/2020
Name: Yunika Upadhayaya
"""
from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
I have added my own version to solve StoneMasonKarel.
StoneMasonKarel should solves the "repair the quad" problem 
where it repairs the quad only if it finds the beeper. 
Program works for all of the sample worlds supplied 
in the starter folder.
"""


def turn_around():
    """
    This function turns the beeper around.
    """
    turn_left()
    turn_left()


def positive_column():
    """
    This function puts the beeper in the whole column. If it finds that the
    column consisted of beeper before, it would come back without picking up
    any beeper.
    """
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()

    turn_around()
    while front_is_clear():
        move()

    turn_left()


def negative_column():
    """
    This function collects all the beeper while coming back that was put before,
    if it finds that no prior beeper were present in the column.
    """
    turn_around()
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()

    if beepers_present():
        pick_beeper()
    turn_left()


def main():

    """
    Implements the functions to obtain the desired output in karel space.
    """
    turn_left()
    while front_is_clear():
        if beepers_present():
            positive_column()

            if front_is_clear():
                move()
                main()
        else:
            put_beeper()
            move()

    if facing_north():
        negative_column()

    if front_is_clear():
        move()
        main()


if __name__ == "__main__":
    """
    This if statement opens up the karel space when calling main().
    """
    run_karel_program()
