"""
File: pyramid.py
----------------
YOUR DESCRIPTION HERE
"""


import tkinter
import time
import random

CANVAS_SIZE = 800
SIZE = 8

N_ROWS = int(CANVAS_SIZE / SIZE)
N_COLS = int(CANVAS_SIZE / SIZE)

def main():
    canvas = make_canvas(CANVAS_SIZE, CANVAS_SIZE, 'Chess Board')
    for row in range(N_ROWS):
        for col in range(N_COLS):
            draw_square(canvas, row, col)
    canvas.mainloop()

def draw_square(canvas, row, col):
    x = col * SIZE
    y = row * SIZE
    color = get_color(row, col)
    canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill=color,outline=color)

def get_color(row, col):
    # if (row + col) % 2 == 1:
    #     return 'white'
    # return 'black'
    return int_to_color(col * row * row)

def int_to_color(value):
    # white is the largest value one can represent
    white_dec = int('ffffff', 16)
    # change your value into "hexadecimal" representation
    hex_str = format(value % white_dec,'x')
    # add 0s to the end until its the right length
    while len(hex_str) < 6:
        hex_str += '0'
    # you now have a color!
    return '#' + hex_str

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas




if __name__ == '__main__':
    main()
