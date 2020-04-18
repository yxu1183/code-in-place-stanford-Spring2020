from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds.
"""


def check_put_beeper():
    """
    This function puts the beeper
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


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    for i in range(3):
        make_building()
        adjacent()


def adjacent():
    """
    This function moves the karel to the adjacent building.
    """
    turn_around()
    move()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()





# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
