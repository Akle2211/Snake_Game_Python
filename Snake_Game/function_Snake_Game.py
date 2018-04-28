# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
#
# This is the function script, to ease read of code.
#
# 28 april 2018


###IMPORTS###
from graphics import *
import time
from random import randint


###FUNCTIONS###

# return where to add a pixel
def amt_to_add(direction, x_or_y):
    if direction == 1 and x_or_y == 'x' or direction == 2 and x_or_y == 'y':
        return 1    # right or down
    elif direction == 3 and x_or_y == 'x' or direction == 0 and x_or_y == 'y':
        return -1   # left or up
    else:
        return 0    # no keys pressed, keep direction the same


# clears all that is in the window
# https://stackoverflow.com/questions/45517677/graphics-py-how-to-clear-the-window
def clear(win):
    for item in win.items[:]:
        item.undraw()
    # win.update()


def check_key(k, direction):
    if k == "Right":
        if direction != 3:  # check if snake isn't going left
            return 1
        return direction

    elif k == "Left":
        if direction != 1:  # check if snake isn't going right
            return 3
        return direction

    elif k == "Up":
        if direction != 2:  # check if snake isn't going down
            return 0
        return direction

    elif k == "Down":
        if direction != 0:  # check if snake isn't going up
            return 2
        return direction

    else:
        return direction


def rand_food_pos(size_of_win):
    temp = [randint(0, size_of_win-1), randint(0, size_of_win-1)]
    return temp


# draws either one set of position or an array of position
# https://stackoverflow.com/questions/998938/handle-either-a-list-or-single-integer-as-an-argument
def drawing_pixel(to_draw, color):
    for sub_list in to_draw:
        # draw food:
        if type(sub_list) is not list:
            sub_list = to_draw
        # draw snake body:
        xcoord = sub_list[0]*step
        ycoord = sub_list[1]*step
        a = Rectangle(Point(xcoord, ycoord), Point(xcoord + step, ycoord + step))
        a.setFill(color)
        a.draw(win)
