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
step = 10
height = 40
width = 40
doexit = False
direction = 0  # 0 up, 1 right, 2 down, 3 left
closest = 4*[100]  # closest coll from snake
win = GraphWin('SNAKE', width*step, height*step, autoflush=False)
win.setBackground('white')

food = rand_pos(width, height)
snakearray = [rand_pos(width, height)]

fps = 0.01  # increase me to make game faster
timeOld = round(time.time() * 1000)


###INIT NEURAL NET###
input_array = [direction, closest[0], closest[1], closest[2], closest[3], food[0], food[1]]
hidden_array = 10*[0]
outputarray = 4*[0]
weights_1 = create_weight_layer(input_array, hidden_array)
weights_2 = create_weight_layer(hidden_array, outputarray)


###RUNNING###
for l in range(100):
    print("made a window !: ", l)
    win = GraphWin('SNAKE', width*step, height*step, autoflush=False)
    win.setBackground('white')
    while doexit == False:  # This is the game loop.
        timeCurrent = round(time.time() * 1000)

        if timeCurrent-timeOld > 1/fps:  # Frames per second stuff

            timeOld = timeCurrent
            clear(win)

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

            ###USER INPUT###
            k = win.checkKey()
            # direction = check_key(k, direction)

    # win.getMouse()  # click mouse to close the game
    win.close()
    print("DONE")
