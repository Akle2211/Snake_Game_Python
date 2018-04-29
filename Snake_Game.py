# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
# 28 april 2018

###IMPORTS###
from graphics import *
import time
from random import randint
from function_Snake_Game import *
from Neural_Network_Function_Snake_Game import *


###FUNCTIONS###
# no functions


def runsnakegamextimes(x):

    ###VARIABLES###
    global step, size_of_win, width, height, win, closest
    step = 10
    size_of_win = width = height = 40
    doexit = False  # for  exiting the game loop
    direction = 0  # 0 up, 1 right, 2 down, 3 left
    closest = 4*[size_of_win]
    win = GraphWin('SNAKE', width*step, height*step, autoflush=False)
    win.setBackground('white')

    food = rand_pos(size_of_win)
    snakearray = [rand_pos(size_of_win)]  # first is the head of the snake

    fps = 0.1  # increase me to make game faster
    refreshrate = 1/fps
    timeOld = round(time.time() * 1000)

    ###VARIABLES NEURAL NETWORK###
    # for calculating closest dis
    closest = closest_any(snakearray, closest, size_of_win)

    score = 0
    begintime = time.time()  # time at the beginning of the game used for fitness
    runtime = time.time()
    fitness = 0

    # neural net stuff
    input_array = calc_input_arr(direction, closest, food, size_of_win)
    hidden_array = 10*[0]
    outputarray = 4*[0]

    weights_1 = create_weight_layer(input_array, hidden_array)
    print("weights1", weights_1)
    # bias1 = rand_list(input_array, 0, 0)

    weights_2 = create_weight_layer(hidden_array, outputarray)
    print("weights2", weights_2)
    # bias2 = rand_list(hidden_array, 0, 0)

    ###RUNNING###
    for l in range(x):
        while doexit == False:  # This is the game loop.
            time.sleep(0.001)
            timeCurrent = round(time.time() * 1000)

            if timeCurrent-timeOld > refreshrate:  # Frames per second stuff
                timeOld = timeCurrent
                clear(win)

            timealive = int(round(runtime-begintime))
            runtime = time.time()
            if timealive > 120:
                doexit = True

                # next position
                snakearray = calc_snake_next_pos(snakearray, direction)

                # wall collision
                if walls(snakearray, size_of_win):
                    print("YOU LOST")
                    doexit = True

                # self collision
                if collision(snakearray):
                    print("CRASHED!")
                    doexit = True

                # food collision
                if collision(snakearray, food):  # food collision ?
                    food = rand_pos(size_of_win)
                    score = score + 10
                    snakearray.append(snakearray[len(snakearray)-1])

                # neural net in the testing
                closest = calc_snake_closest(snakearray, size_of_win)
                input_array = calc_input_arr(direction, closest, food, size_of_win)
                print(input_array)
                outputarray = neural_network(input_array, weights_1, weights_2)
                print(outputarray)

                # drawing everything
                drawing_pixel(snakearray, 'black', step, win)
                drawing_pixel(food, 'red', step, win)
                update()

                # checking user input
                k = win.checkKey()
                if k == "e":
                    doexit = True  # Click e to exit!

                # current direction
                # direction = check_key(k, direction)
                direction = dir_of_neural_net(outputarray)

        win.getMouse()  # click mouse to close the game
        win.close()
        print("DONE")


runsnakegamextimes(100)
