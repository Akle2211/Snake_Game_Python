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


def calculate_layer(prev_layer, prev_weight_layer):
    total = 0
    temp = []
    for i in range(len(prev_weight_layer)):
        for neuron, weight in zip(prev_layer, prev_weight_layer[i]):
            total = total + (neuron*weight)
        temp.append(total)
        total = 0
    return temp
# https: // www.programiz.com/python-programming/methods/built-in/zip


# returns a leyr of weights1
def create_weight_layer(prev_layer, next_layer):
    weights = []
    for neuron in next_layer:
        weights.append(rand_list(prev_layer))
    return weights


def neural_network(input_array, weights_1, weights_2):
    input_array = sigmoid_neurons(input_array)
    hidden_array = sigmoid_neurons(calculate_layer(input_array, weights_1))
    output_array = sigmoid_neurons(calculate_layer(hidden_array, weights_2))
    return output_array


def dir_of_neural_net(outputarray):
    temp = outputarray.index(max(outputarray))
    print(temp)
    return temp


def sigmoid_neurons(neurons):
    temp = []
    for neuron in neurons:
        temp.append(sigmoid_neg1_to_1(neuron))
    return temp
