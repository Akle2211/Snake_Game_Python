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

# return where to add a pixel, it is used in the calc_snake_next_pos()
# so that the snake never travels in diagonal by mistake
# basically, it will add +1 at the snake x or y head position.
# the else at the end should never be attained in normal condition.
# otherwise, the snake would stop moving.
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
    # win.update()  #update() is done in the running game


# draws either one set of position or an array of position
# https://stackoverflow.com/questions/998938/handle-either-a-list-or-single-integer-as-an-argument
def drawing_pixel(to_draw, color, step, win):
    for sub_list in to_draw:
        if type(sub_list) is not list:  # draw food:
            sub_list = to_draw

        xcoord = sub_list[0]*step  # else draw snake body
        ycoord = sub_list[1]*step
        a = Rectangle(Point(xcoord, ycoord), Point(xcoord + step, ycoord + step))
        a.setFill(color)
        a.draw(win)


#return a random set of position
def rand_pos(width, height='fool'):
    if height == 'fool':
        height = width
    return [randint(0, width-1), randint(0, height-1)]


#check_key can work with both user input and neural output
def check_key(k, direction):
    if k == "Right" or k == 1:
        if direction != 3:  # check if snake isn't going left
            return 1
        return direction
    elif k == "Left" or k == 3:
        if direction != 1:  # check if snake isn't going right
            return 3
        return direction
    elif k == "Up" or k == 0:
        if direction != 2:  # check if snake isn't going down
            return 0
        return direction
    elif k == "Down" or k == 2:
        if direction != 0:  # check if snake isn't going up
            return 2
        return direction
    else:
        return direction


# check if a food collision happened
def food_coll(snakearray, food):
    if snakearray[0][0] == food[0] and snakearray[0][1] == food[1]:  # check if the food has been eaten
        return True
    return False


# calculate the next position of the snake
def calc_snake_next_pos(snakearray, direction):
    def amt_to_add(direction, x_or_y):
        if direction == 0 and x_or_y == 'x' or direction == 2 and x_or_y == 'y':
            return 1    # right or down
        elif direction == 3 and x_or_y == 'x' or direction == 0 and x_or_y == 'y':
            return -1   # left or up
        else:
            return 0    # no keys pressed, keep direction the same
    headnewposarray = [snakearray[0][0] + amt_to_add(direction, 'x'),
                       snakearray[0][1] + amt_to_add(direction, 'y')]
    snakearray.insert(0, headnewposarray)  # add head at beginning
    del snakearray[len(snakearray)-1]  # delete last tail
    return snakearray


def closest_any(snakearray, width, height='fool'):
    closest = 4*[100]
    if height == 'fool':
        height = width

    for i in range(len(snakearray[1:])):
        if snakearray[0][0] == snakearray[i+1][0]:  # body's in the same vertical line as head
            if snakearray[0][1] - snakearray[i+1][1] > 0:   # body up head
                if closest[0] > abs(snakearray[0][1] - snakearray[i+1][1]):
                    closest[0] = abs(snakearray[0][1] - snakearray[i+1][1])
            else:                                           # else body down head
                if closest[2] > abs(snakearray[0][1] - snakearray[i+1][1]):
                    closest[2] = abs(snakearray[0][1] - snakearray[i+1][1])
        if snakearray[0][1] == snakearray[i+1][1]:  # body's in the same horizontal line as head
            if snakearray[0][0] - snakearray[i+1][0] > 0:   # body left head
                if closest[3] > abs(snakearray[0][0] - snakearray[i+1][0]):
                    closest[3] = abs(snakearray[0][0] - snakearray[i+1][0])
            else:                                           # else body right head
                if closest[1] > abs(snakearray[0][0] - snakearray[i+1][0]):
                    closest[1] = abs(snakearray[0][0] - snakearray[i+1][0])

    if closest[0] > snakearray[0][1]:  # up wall
        closest[0] = snakearray[0][1]
    if closest[2] > height - snakearray[0][1]:  # down wall
        closest[2] = height - snakearray[0][1]
    if closest[3] > snakearray[0][0]:  # left wall
        closest[3] = snakearray[0][0]
    if closest[1] > width - snakearray[0][0]:  # right wall
        closest[1] = width - snakearray[0][0]

    print("closest: ", closest)
    print("snakearray: ", snakearray)
    return closest


def wall_or_self_coll(closest):
    if min(closest) <= 0:
        return True
    return False
