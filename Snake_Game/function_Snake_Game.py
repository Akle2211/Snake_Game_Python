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


# draws either one set of position or an array of position
# https://stackoverflow.com/questions/998938/handle-either-a-list-or-single-integer-as-an-argument
def drawing_pixel(to_draw, color, step, win):
    for sub_list in to_draw:
        if type(sub_list) is not list:  # draw food:
            sub_list = to_draw

        # else draw snake body
        xcoord = sub_list[0]*step
        ycoord = sub_list[1]*step
        a = Rectangle(Point(xcoord, ycoord), Point(xcoord + step, ycoord + step))
        a.setFill(color)
        a.draw(win)


def rand_pos(size_of_win):
    return [randint(0, size_of_win-1), randint(0, size_of_win-1)]


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


# calculate the next position of the snake
def calc_snake_next_pos(snakearray, direction):
    headnewposarray = [snakearray[0][0] + amt_to_add(direction, 'x'),
                       snakearray[0][1] + amt_to_add(direction, 'y')]
    snakearray.insert(0, headnewposarray)  # add head at beginning
    del snakearray[len(snakearray)-1]  # delete last tail
    return snakearray


# returns the closest wall it is into
def calc_snake_closest(snakearray, size_of_win):
    closestup = snakearray[0][1]
    closestright = size_of_win - snakearray[0][0]
    closestdown = size_of_win - snakearray[0][1]
    closestleft = snakearray[0][0]
    temp = [closestup, closestright, closestdown, closestleft]
    return temp


# calculate the distance from wall/body
def closest_any(snakearray, closest, size_of_win):
    # First find the closest distance from the body to the snake
    for i in range(len(snakearray)-1):

        # is body right to head ?
        if snakearray[0][0] - snakearray[i+1][0] < 0:
            if abs(snakearray[0][0] - snakearray[i+1][0]) < closest[1]:
                closest[1] = abs(snakearray[0][0] - snakearray[i+1][0])
        else:
            # no, closestright is the wall
            closest[1] = size_of_win - snakearray[0][0]

        # is body left to head ?
        if snakearray[0][0] - snakearray[i+1][0] > 0:
            if snakearray[0][0] - snakearray[i+1][0] < closest[3]:
                closest[3] = abs(snakearray[0][0] - snakearray[i+1][0])
        else:
            # no, closestleft is the wall
            closest[3] = size_of_win - snakearray[0][0]

        # is body above head ?
        if snakearray[0][1] - snakearray[i+1][1] > 0:
            if snakearray[0][1] - snakearray[i+1][1] < closest[0]:
                closest[0] = abs(snakearray[0][1] - snakearray[i+1][1])
        else:
            # no, closestup is the wall
            closest[0] = size_of_win - snakearray[0][0]

        # is body below head ?
        if snakearray[0][1] - snakearray[i+1][1] < 0:
            if abs(snakearray[0][1] - snakearray[i+1][1]) < closest[2]:
                closest[2] = abs(snakearray[0][1] - snakearray[i+1][1])
        else:  # no, closestdown is the wall
            closest[2] = size_of_win - snakearray[0][0]

    return closest


def walls(snakearray, size_of_win):
    if snakearray[0][0] == size_of_win or snakearray[0][1] == size_of_win or snakearray[0][0] == -1 or snakearray[0][1] == -1:
        print("YOU LOST")
        return True


def timing():
    pass  # aint done yet

###FILING SYSTEM FUNCTIONS###


def writing_files(file, values):
    for value in values:  # Output weights
        file.write(str(value))
        if values.index(value) < len(values):
            file.write(",")
    file.close()