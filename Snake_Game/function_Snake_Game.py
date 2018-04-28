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

# SIGMOID FUNCTION
def sigmoid(x):  # not going to define e to make it easier, just going to use the decimal value for it
    return 1/((2.718281828459**-x) + 1)


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


# check if a collision happened
def collision(snakearray, food=2):
    if type(food) is list:
        if snakearray[0][0] == food[0] and snakearray[0][1] == food[1]:  # check if the food has been eaten
            return True
        return False

    for body_part in snakearray[1:]:
        if snakearray[0][0] == body_part[0] and snakearray[0][1] == body_part[1]:
            return True
    return False


def collision_food(snakearray, food):
    if snakearray[0][0] == food[0] and snakearray[0][1] == food[1]:  # check if the food has been eaten
        return True
    return False


def timing():
    pass  # aint done yet
