"""
Date Created: 04/18/2020
Name: Yunika Upadhayaya
"""

from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
TripleKarel paints the exterior of three buildings in a given
world, as described in the Assignment 1 handout. Program works 
for all of the Triple sample worlds.
"""


def turn_around():
    """
    This function turns the beep around.
    """
    for i in range(2):
        turn_left()


def turn_right():
    """
    This function turns the beeper right.
    """
    for i in range(3):
        turn_left()


def check_put_beeper():
    """
    This function puts the beeper along the sides of the building and
    moves forward.
    """
    put_beeper()
    turn_right()
    move()
    turn_left()


def make_building():
    """
    This function paints all of the buildings (rectangle) present in
    the world by placing beepers along three of the sides of each of
    the building.
    """
    for i in range(3):
        turn_left()
        while front_is_blocked():
            check_put_beeper()
        move()


def adjacent():
    """
    This function moves the karel to the adjacent building.
    """
    turn_around()
    move()


def main():
    """
    Karel completes the desired work by calling the appropriate
    function in the main.

    """
    for i in range(3):
        make_building()
        adjacent()
    turn_left()


if __name__ == "__main__":
    """
    This if statement opens up the Karel space when calling main().
    """
    run_karel_program()
