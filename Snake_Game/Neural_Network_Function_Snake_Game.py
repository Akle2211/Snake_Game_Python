# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
#
# This is the neural function script, to ease read of code.
#
# 28 april 2018


###IMPORTS###
from graphics import *
import time
from random import randint
import random


###NEURAL NETWORK FUNCTIONS###
# SIGMOID FUNCTION
def sigmoid_neg1_to_1(x):  # not going to define e
    return (2/(1 + 2.718281828459**-x)) - 1


def rand_list(input_neurons, low=-1, high=1):
    temp = []
    if type(input_neurons) is int:
        temp.append(randint(low, high))
    else:
        for neuron in input_neurons:
            temp.append(randint(low, high))
    return temp


# calculate the input array
def calc_input_arr(direction, closest, food, width, height='fool'):
    if height == 'fool':
        height = width
    temp = [direction,
            closest[0]/height,
            closest[1]/width,
            closest[2]/height,
            closest[3]/width,
            food[0]/width,
            food[1]/height,
            1]
    return temp


# returns the next sets of neuron, the next layer.
def calculate_layer(prev_layer, prev_weight_layer, bias=False):
    total = 0
    temp = []
    for i in range(len(prev_weight_layer)):
        for neuron, weight in zip(prev_layer, prev_weight_layer[i]):
            total = total + (neuron*weight)
        temp.append(total)
        total = 0
    if bias:    # bias is necessary in the hidden layer, but not in the output !
        temp.append(1)
    return temp
# https: // www.programiz.com/python-programming/methods/built-in/zip


def neural_network(input_array, weights_1, weights_2):
    input_array = sigmoid_neurons(input_array)
    hidden_array = sigmoid_neurons(calculate_layer(input_array, weights_1, True))
    output_array = sigmoid_neurons(calculate_layer(hidden_array, weights_2))
    return output_array


# returns a leyr of weights1
def create_weight_layer(prev_layer, next_layer):
    weights = []
    for neuron in next_layer:
        weights.append(rand_list(prev_layer))
    return weights


def dir_of_neural_net(outputarray):
    temp = outputarray.index(max(outputarray))
    print(temp)
    return temp


def sigmoid_neurons(neurons):
    temp = []
    for neuron in neurons:
        temp.append(sigmoid_neg1_to_1(neuron))
    return temp


def swap(array1, array2, first):  # array1 is the fittest network (first is there to check which array to give back)(17 subarray (including fitness score)
    if first == 1:
        for i in range(15):
            random_num = random.randint(0, 6)
            # take weight from array two and assign it to array1 (2 => 1)
            array1[i+1][random_num] = array2[i+1][random_num]
        return array1
    if first == 2:
        for i in range(15):
            random_num = random.randint(0, 6)
            # take weight from array two and assign it to array1 (1 => 2)
            array2[i+1][random_num] = array1[i+1][random_num]
        return array2
