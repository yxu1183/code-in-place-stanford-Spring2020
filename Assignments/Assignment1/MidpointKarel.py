"""
Date Created: 04/21/2020
Name: Yunika Upadhayaya
"""
from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
MidpointKarel leaves a beeper on the corner closest to the 
center of 1st Street (or either of the two central corners if 
1st Street has an even number of corners).  Karel puts down additional 
beepers as it looks for the midpoint, but picks them up again 
before it stops. This code works for all the worlds.
"""


def turn_around():
    """
    This function turns the beeper right.
    """
    turn_left()
    turn_left()


def check_edge():
    """
    This function checks for the edge and puts the beeper while
    returning back - it helps in checking the width of the 1st street and
    eventually its midpoint.
    """
    for i in range(2):
        while front_is_clear():
            move()
        put_beeper()
        turn_around()


def main():
    """
    Implements functions to obtain required result in karel space.
    """
    check_edge();
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()
            turn_around()
            move()
            put_beeper()
    turn_around()
    while no_beepers_present():
        move()
    pick_beeper()


if __name__ == "__main__":
    """
    This if statement opens up the karel space while running main.
    """
    run_karel_program()
