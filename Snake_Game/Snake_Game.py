# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
# 28 april 2018

###IMPORTS###
from graphics import *
import time
from random import randint
from function_Snake_Game import *


###FUNCTIONS###
def rand_pos():
    return [randint(0, size_of_win-1), randint(0, size_of_win-1)]


def drawing_pixel(to_draw, color):
    a = calculate_drawing(to_draw, color, step)
    a.draw(win)


###VARIABLES###
step = 10
size_of_win = width = height = 40
win = GraphWin('SNAKE', width*step, height*step, autoflush=False)
win.setBackground('white')

food = rand_pos()
doexit = False  # for  exiting the game loop
direction = 0  # 0 up, 1 right, 2 down, 3 left

snakearray = [rand_pos()]  # first is the head of the snake

fps = 0.005  # decrease me to make game faster
refreshrate = 1/fps
timeOld = round(time.time() * 1000)

###VARIABLES NEURAL NETWORK###
# for calculating closest dis
# closestup = snakearray[0][1]
# closestright = size_of_win - snakearray[0][0]
# closestdown = size_of_win - snakearray[0][1]
# closestleft = snakearray[0][0]
closestup = 22
closestright = 23
closestdown = 18
closestleft = 18
food = [20, 20]

score = 0
begintime = time.time()  # time at the beginning of the game used for fitness
runtime = time.time()
fitness = 0


###ARRAYS NEURAL NETWORK###
# for network i will just try random array
input_array = [closestup/size_of_win, closestdown/size_of_win, closestleft/size_of_win,
               closestright/size_of_win, food[0]/size_of_win, food[1]/size_of_win]  # add the food coordinates

print("input: ", input_array)
input_array = sigmoid_neurons(input_array)
print("input_array trough sigmoid: ", input_array)
# weights_1 = [randomize_weight(input_array),
#              randomize_weight(input_array),
#              randomize_weight(input_array),
#              randomize_weight(input_array),
#              randomize_weight(input_array),
#              randomize_weight(input_array)]
weights_1 = [[1, 2, -2, 3, 0, -1],
             [1, 2, -2, 3, 0, -1],
             [1, 2, -2, 3, 0, -1],
             [1, 2, -2, 3, 0, -1],
             [1, 2, -2, 3, 0, -1],
             [1, 2, -2, 3, 0, -1]]
print("weights_1", weights_1)
# bias1 = randomize_weight(input_array)
bias1 = [1, 1, 1, 1, 1, 1]


hidden_array = calculate_layer(input_array, weights_1, bias1, 6)
print("hidden_array: ", hidden_array)
hidden_array = sigmoid_neurons(hidden_array)
print("hidden_array trough sigmoid: ", hidden_array)
# weights_2 = [randomize_weight(input_array),
#              randomize_weight(input_array),
#              randomize_weight(input_array),
#              randomize_weight(input_array),
#              randomize_weight(input_array),
#              randomize_weight(input_array)]
weights_2 = [[-1, 0, -2, 3, 3, -1],
             [-1, 0, -2, 3, 3, -1],
             [-1, 0, -2, 3, 3, -1],
             [-1, 0, -2, 3, 3, -1],
             [-1, 0, -2, 3, 3, -1],
             [-1, 0, -2, 3, 3, -1]]

print("weights2", weights_2)
# bias2 = randomize_weight(hidden_array)
bias2 = [1, 1, 1, 1, 1, 1]

outputarray = calculate_layer(hidden_array, weights_2, bias2, 4)
print("outputarray: ", outputarray)
outputarray = sigmoid_neurons(outputarray)
print("outputarray trough sigmoid: ", outputarray)

print("")
print("")


###RUNNING###
while doexit == False:  # This is the game loop.
    time.sleep(0.001)
    timeCurrent = round(time.time() * 1000)

    if timeCurrent-timeOld > refreshrate:  # Frames per second stuff
        timeOld = timeCurrent
        clear(win)

        # c = Rectangle(Point(0, 0), Point(400, 400))
        # c.setFill('white')                                  #this code isn't necessary anymore !
        # c.draw(win)  # clear screen

        headnewposarray = [snakearray[0][0] +
                           amt_to_add(direction, 'x'), snakearray[0][1] + amt_to_add(direction, 'y')]

        snakearray.insert(0, headnewposarray)  # add head at beginning
        del snakearray[len(snakearray)-1]  # delete last tail

        if collision(snakearray):       # self collision ?
            print("CRASHED!")
            doexit = True

        if collision(snakearray, food):  # food collision ?
            food = rand_pos()
            print("YUM")
            # add the latest element to the snake's body
            snakearray.append(snakearray[len(snakearray)-1])

        drawing_pixel(snakearray, 'black')
        drawing_pixel(food, 'red')
        update()

        k = win.checkKey()  # register the last key that was pressed
        if k == "e":
            doexit = True  # Click e to exit!
        direction = check_key(k, direction)


win.getMouse()  # click mouse to close the game
win.close()
print("DONE")
# checkKey() returns the last key that was presssed
