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

# luca's sigmoid:
def sigmoid_neg1_to_1(x):  # not going to define e
    return (2/(1 + 2.718281828459**-x)) - 1

# Henrijs's sigmoid
def sigmoid(x):  # not going to define e
    return 1/(1 + 2.718281828459**-x)


# takes in a list of neurons(input_neurons), then create a list 
# of random integers the size of the list.
# if input_neurons is instead a number, it will return a list 
# the size of that number, full of random integers
# the default random is -5,5, but it can be set very simply.
# rand_list(3,-2,2) = [2,-1,0]
def rand_list(input_neurons, low=-5, high=5):
    temp = []
    if type(input_neurons) is int:
        temp.append(randint(low, high))
    else:
        for neuron in input_neurons:
            temp.append(randint(low, high))
    return temp


# calculate the input array
# this is an old function not to be used anymore.
# it is better to directly put the input information directly in the 
# input array.
# this function speak for itself though.
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
            1] #1 is the bias
    return temp


# returns the next sets of neuron, the next layer.
#zip can be used to walk 2 list at the same time (look link)
# https: // www.programiz.com/python-programming/methods/built-in/zip
#calculate_layer basically calculate the hidden or the output layer of our neural network
#it is used in the neural network function mainly
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


# main function, it takes the input array and the weights_1,
# then create the hidden array, which is used with the weights_2
# to create the output array !
def neural_network(input_array, weights_1, weights_2):
    input_array = sigmoid_neurons(input_array)
    hidden_array = sigmoid_neurons(calculate_layer(input_array, weights_1, True))
    output_array = sigmoid_neurons(calculate_layer(hidden_array, weights_2))
    return output_array


# returns a layer of weights, depending on the neurons surrounding it
# for example, if prev_layer = 3 and next_layer = 4, 
# create_weight_layer will return [[x,x,x],[x,x,x],[x,x,x],[x,x,x]]
# x being random integers
def create_weight_layer(prev_layer, next_layer):
    weights = []
    for neuron in next_layer: # loops 4 times
        weights.append(rand_list(prev_layer)) #create a list of 3 random integers
    return weights

# takes the output array, and returns the direction, 
# based on the max value, the highest probability
def dir_of_neural_net(outputarray):
    temp = outputarray.index(max(outputarray))
    return temp


# takes the values of a layer of neurons, and return their sigmoid.
# for example, [0.72, 4, -2,0] will return [sigm(0.72), sigm(4), sigm(-2), sigm(0)]
# IT DEPENDS ON WHICH SIGMOID IS USED (Henrijs's or Luca's sigmoid !!!)
def sigmoid_neurons(neurons):
    temp = []
    for neuron in neurons:
        temp.append(sigmoid_neg1_to_1(neuron)) # change sigmoid here !!!
    return temp


# this function was created by Henrijs, and i cannot define iteasily without mistake.
#it is supposed to randomly swap the weights from 2 different neural network (the parents)
#and then returns the child.
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
