# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
#
# this is Henrijs's script
#
# 28 april 2018


###IMPORTS###
from graphics import *
import time
from random import randint
import random
from function_Snake_Game import *
from Files_function import *
from Neural_Network_Function_Snake_Game import *

###FUNCTIONS###


def runsnakegamextimes(x):
    for k in range(x):

        ###VARIABLES###
        # for calculating closest dis and files
        aweights1 = open(str(k)+"weights1", "w")
        aweights11 = open(str(k)+"weights11", "w")
        aweights111 = open(str(k)+"weights111", "w")
        aweights1111 = open(str(k)+"weights1111", "w")
        aweights11111 = open(str(k)+"weights11111", "w")
        aweights111111 = open(str(k)+"weights111111", "w")
        aweights1111111 = open(str(k)+"weights1111111", "w")
        file_weights_1 = [aweights1, aweights11, aweights111,
                          aweights1111, aweights11111, aweights111111, aweights1111111]

        abiashidden1 = open(str(k)+"biashidden1", "w")

        aweights2 = open(str(k)+"weights2", "w")
        aweights22 = open(str(k)+"weights22", "w")
        aweights222 = open(str(k)+"weights222", "w")
        aweights2222 = open(str(k)+"weights2222", "w")
        aweights22222 = open(str(k)+"weights22222", "w")
        aweights222222 = open(str(k)+"weights222222", "w")
        aweights2222222 = open(str(k)+"weights2222222", "w")
        file_weights_2 = [aweights2, aweights22, aweights222,
                          aweights2222, aweights22222, aweights222222, aweights2222222]

        thetotal = 0

        score = 0
        begintime = time.time()  # time at the beginning of the game used for fitness
        runtime = time.time()
        fitness = 0

        step = 10
        size_of_win = width = height = 40
        win = GraphWin('SNAKE', width*step, height*step, autoflush=False)
        win.setBackground('white')

        food = rand_pos(size_of_win)
        doexit = False  # for  exiting the game loop
        direction = 0  # 0 up, 1 right, 2 down, 3 left

        snakearray = [rand_pos(size_of_win)]  # first is the head of the snake

        fps = 1  # increase me to make game faster
        refreshrate = 1/fps
        timeOld = round(time.time() * 1000)

        ###VARIABLES NEURAL NETWORK###
        # for calculating closest dis
        closest = closest_any(snakearray, size_of_win)

        ###ARRAYS###
        # for netowrk i will just try random array
        input_array = calc_input_arr(direction, closest, food, size_of_win)
        print("input_array: ", input_array)
        hidden_array = 7*[0]
        outputarray = 4*[0]
        weights_1 = create_weight_layer(input_array, hidden_array)
        print("weights_1: ", weights_1)
        weights_2 = create_weight_layer(hidden_array, outputarray)
        print(weights_1)
        print(weights_2)

        # biashidden1 = []
        # biasoutput = []
        #
        # for i in range(7):
        #     biashidden1.append(rand_list())
        # for i in range(4):
        #     biasoutput.append(rand_list())

        def neuralnetwork(input_array, weights_1, biashidden1, weights_2):

            hiddenneurons = sigmoid_neurons(calculate_layer(input_array, weights_1))
            outputneurons = sigmoid_neurons(calculate_layer(hiddenneuron, weights_2))

            return dir_of_neural_net(outputneuron)

        ###RUNNING###
        while doexit == False:  # This is the game loop.
            time.sleep(0.001)
            timeCurrent = round(time.time() * 1000)

            if timeCurrent-timeOld > refreshrate:  # Frames per second stuff
                timeOld = timeCurrent
                clear(win)

                c = Rectangle(Point(0, 0), Point(400, 400))
                c.setFill('white')
                c.draw(win)  # clear screen

                runtime = time.time()
                timealive = int(round(runtime-begintime))
                fitness = timealive+score*10

                ###INIT NEURAL NET###
                closest = closest_any(snakearray, height, width)
                input_array = [direction, closest[0], closest[1],
                               closest[2], closest[3], food[0], food[1]]
                outputarray = neural_network(input_array, weights_1, weights_2)
                direction = dir_of_neural_net(outputarray)

                ###POS AND COLL###
                snakearray = calc_snake_next_pos(snakearray, direction)
                if food_coll(snakearray, food):
                    food = rand_pos(size_of_win)
                    score = score + 10
                    snakearray.append(snakearray[len(snakearray)-1])
                if wall_or_self_coll(closest):
                    print("YOU LOST")
                    doexit = True

                ###DRAW###
                drawing_pixel(snakearray, 'black', step, win)
                drawing_pixel(food, 'red', step, win)
                update()

                neuraldirection = neural_network(input_array, weights_1, weights_2)
                direction = check_key(neuraldirection, direction)

                k = win.checkKey()  # register the last key that was pressed
                if k == "e":
                    doexit = True  # Click e to exit!
                #direction = check_key(k, direction)

        ###GOOD###
        win.close()
        print("len of input_array: ", len(input_array))
        print("len of weights_1: ", len(weights_1))
        print("len of file_weights_1: ", len(file_weights_1))

        ###GOOD###
        for i in range(len(hidden_array)):
            writing_files(file_weights_1[i], weights_1[i])
        for i in range(len(outputarray)):
            writing_files(file_weights_2[i], weights_2[i])
        #writing_files(abiashidden1, biashidden1)


runsnakegamextimes(100)
