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


def timing():
    pass  # aint done yet


###NEURAL NETWORK FUNCTIONS###
# SIGMOID FUNCTION
def sigmoid_neg1_to_1(x):  # not going to define e to make it easier, just going to use the decimal value for it
    return (2/(1 + 2.718281828459**-x)) - 1


def rand_list(input_neurons, low=-3, high=3):
    temp = []
    for neuron in input_neurons:
        temp.append(randint(low, high))
    return temp


# calculate the input array
def calc_input_arr(direction, closest, food, size_of_win):
    temp = [direction,
            closest[0]/size_of_win,
            closest[1]/size_of_win,
            closest[2]/size_of_win,
            closest[3]/size_of_win,
            food[0]/size_of_win,
            food[1]/size_of_win,
            1]
    return temp


def calculate_layer(prev_layer, prev_weight_layer, desired_len):
    total = 0
    temp = []
    for i in range(len(prev_weight_layer)):
        for neuron, weight in zip(prev_layer, prev_weight_layer[i]):
            total = total + (neuron*weight)
        temp.append(total)
        total = 0
    return temp
# https: // www.programiz.com/python-programming/methods/built-in/zip


def create_weight_layer(prev_layer, next_layer):
    weights = []
    for neuron in next_layer:
        weights.append(rand_list(prev_layer))
    return weights


def neural_network(input_array, weights_1, weights_2):
    input_array = sigmoid_neurons(input_array)
    hidden_array = sigmoid_neurons(calculate_layer(input_array, weights_1, 6))
    outputarray = sigmoid_neurons(calculate_layer(hidden_array, weights_2, 4))
    return outputarray


def dir_of_neural_net(outputarray):
    temp = outputarray.index(max(outputarray))
    print(temp)
    return temp


def sigmoid_neurons(neurons):
    temp = []
    for neuron in neurons:
        temp.append(sigmoid_neg1_to_1(neuron))
    return temp
