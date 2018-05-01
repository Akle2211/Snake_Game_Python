# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
# 28 april 2018
#
# V1 version of the original Snake_Game.py

###IMPORTS###
from graphics import *
import time
from random import randint
from function_Snake_Game import *
from Neural_Network_Function_Snake_Game import *
from Files_function import *


###VARIABLES###
gamespeed = 1
step = 10
height = 40
width = 40
doexit = False
direction = 0  # 0 up, 1 right, 2 down, 3 left
closest = 4*[100]  # closest coll from snake


food = rand_pos(width, height)
snakearray = [rand_pos(width, height)]
score = 0
fitness = 0

fps = gamespeed  # increase me to make game faster
timeOld = round(time.time() * 1000)


###INIT NEURAL NET###
input_array = [direction, closest[0], closest[1], closest[2], closest[3], food[0], food[1]]
hidden_array = 10*[0]
outputarray = 4*[0]
weights_1 = create_weight_layer(input_array, hidden_array)
weights_2 = create_weight_layer(hidden_array, outputarray)


###RUNNING###
for l in range(100):

    ###REINITIALIZE###
    time_since_beginning_run = time.time()
    begintime = time.time() * 1000
    doexit = False
    score = 0

    food = rand_pos(width, height)
    snakearray = [rand_pos(width, height)]
    weights_1 = create_weight_layer(input_array, hidden_array)
    weights_2 = create_weight_layer(hidden_array, outputarray)

    ###WRITE WEIGHTS TO FOLDER###
    # CONVERT ALL THE ARRAYS TO WRITEABLE FORMAT
    for i in range(len(weights_1)):
        write_file_to_subfolder("GENERATION0", str(l) + "weights_1", "weights" +
                                "1"*i, convert_arr_to_writeable_str(weights_1[i]))
    for i in range(len(weights_2)):
        write_file_to_subfolder("GENERATION0", str(l) + "weights_2", "weights" +
                                "2"*i, convert_arr_to_writeable_str(weights_1[i]))

    print("made a window !: ", l)
    win = GraphWin('SNAKE', width*step, height*step, autoflush=False)
    win.setBackground('white')

    ###ONE GAME RUNNING###
    while doexit == False:  # This is the game loop.
        timeCurrent = round(time.time() * 1000)

        if timeCurrent-timeOld > 1/fps:  # Frames per second stuff

            ###TIME AND WIN CLEANUP###
            timeOld = timeCurrent
            clear(win)

            ###INIT NEURAL NET###
            closest = closest_any(snakearray, height, width)
            input_array = [direction, closest[0], closest[1],
                           closest[2], closest[3], food[0], food[1]]
            direction = dir_of_neural_net(neural_network(input_array, weights_1, weights_2))

            ###POS AND COLL AND TIMING###
            snakearray = calc_snake_next_pos(snakearray, direction)
            if food_coll(snakearray, food):
                food = rand_pos(width, height)
                score = score + 10
                snakearray.append(snakearray[len(snakearray)-1])
            if wall_or_self_coll(closest) or istimeup(time_since_beginning_run, gamespeed):
                print("YOU LOST")
                # write fitness score at the end of game
                write_file_to_subfolder("GENERATION0", str(l) + "fitness", "fitness", str(fitness))
                doexit = True

            ###FITNESS SCORE###
            fitness = calc_fit(time_since_beginning_run, gamespeed, score)  # NEW!  :3 -- 'noice!'

            ###DRAW###
            drawing_pixel(snakearray, 'black', step, win)
            drawing_pixel(food, 'red', step, win)
            update()

            ###USER INPUT###
            #k = win.checkKey()
            # direction = check_key(k, direction)

    # win.getMouse()  # click mouse to close the game
    win.close()
    print("DONE")
