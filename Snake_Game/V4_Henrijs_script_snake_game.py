# -*- coding: cp1252 -*-
# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
# 28 april 2018

###IMPORTS###
from graphics import *
import time
from random import randint
import random

###FUNCTIONS###
# return where to add a pixel
# SIGMOID FUNCTION


def runsnakegamextimes(x):
    avg_fitness = 0
    for k in range(x):
        def sigmoid(x):  # not going to define e to make it easier, just going to use the decimal value for it
            return (2.718281828459**x)/(2.718281828459**x + 1)

        def calcappledist(apple, snake):
            return sigmoid(apple-snake)

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

        def checkdirection(direction, neuraldirection):
            if direction == 0 and neuraldirection == 2:
                return 0
            if direction == 2 and neuraldirection == 0:
                return 2
            if direction == 1 and neuraldirection == 3:
                return 1
            if direction == 3 and neuraldirection == 1:
                return 3
            else:
                return neuraldirection

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
                return direction    # no keys were pressed

        def rand_food_pos():
            return [randint(0, size_of_win-1), randint(0, size_of_win-1)]

        # draws either one set of position or an array of positions
        # https://stackoverflow.com/questions/998938/handle-either-a-list-or-single-integer-as-an-argument
        def drawing_pixel(to_draw, color):
            for sub_list in to_draw:
                # draw food:
                if type(sub_list) is not list:
                    sub_list = to_draw
                # draw snake body:
                xcoord = sub_list[0]*step
                ycoord = sub_list[1]*step
                a = Rectangle(Point(xcoord, ycoord), Point(xcoord + step, ycoord + step))
                a.setFill(color)
                a.draw(win)

        ###VARIABLES###
        # for calculating closest dis and files

        thetotal = 0
        closestup = 40
        closestright = 40
        closestdown = 40
        closestleft = 40
        applex = 10
        appley = 10

        score = 0
        begintime = time.time()  # time at the beginning of the game used for fitness
        runtime = time.time()
        fitness = 0

        step = 10
        size_of_win = width = height = 40
        win = GraphWin('SNAKE', width*step, height*step, autoflush=False)
        win.setBackground('white')

        food = rand_food_pos()
        doexit = False  # for  exiting the game loop
        direction = 0  # 0 up, 1 right, 2 down, 3 left

        snakearray = [[10, 10]]  # first is the head of the snake

        fps = 1.0  # decrease me to make game slower
        refreshrate = 1/fps
        timeOld = round(time.time() * 1000)

        ###ARRAYS###
        # for netowrk i will just try random array
        inputarray = [closestup, closestdown, closestleft,
                      closestright, applex, appley]  # add the apple coordinates

        aweights1 = open(str(k)+"weights1", "r")
        aweights11 = open(str(k)+"weights11", "r")
        aweights111 = open(str(k)+"weights111", "r")
        aweights1111 = open(str(k)+"weights1111", "r")
        aweights11111 = open(str(k)+"weights11111", "r")
        aweights111111 = open(str(k)+"weights111111", "r")
        aweights1111111 = open(str(k)+"weights1111111", "r")
        abiashidden1 = open(str(k)+"biashidden1", "r")
        aweights2 = open(str(k)+"weights2", "r")
        aweights22 = open(str(k)+"weights22", "r")
        aweights222 = open(str(k)+"weights222", "r")
        aweights2222 = open(str(k)+"weights2222", "r")
        aweights22222 = open(str(k)+"weights22222", "r")
        aweights222222 = open(str(k)+"weights222222", "r")
        aweights2222222 = open(str(k)+"weights2222222", "r")
        abiasoutput = open(str(k)+"biasoutput", "r")
        afitness = open(str(k)+"fitness", "w")

        weights1 = aweights1.read().split(',')
        weights11 = aweights11.read().split(',')
        weights111 = aweights111.read().split(',')
        weights1111 = aweights1111.read().split(',')
        weights11111 = aweights11111.read().split(',')
        weights111111 = aweights111111.read().split(',')
        weights1111111 = aweights1111111.read().split(',')
        biashidden1 = abiashidden1.read().split(',')
        weights2 = aweights2.read().split(',')
        weights22 = aweights22.read().split(',')
        weights222 = aweights222.read().split(',')
        weights2222 = aweights2222.read().split(',')
        weights22222 = aweights22222.read().split(',')
        weights222222 = aweights222222.read().split(',')
        weights2222222 = aweights2222222.read().split(',')
        biasoutput = abiasoutput.read().split(',')

        for i in range(7):
            weights1[i] = int(weights1[i])
            weights11[i] = int(weights11[i])
            weights111[i] = int(weights111[i])
            weights1111[i] = int(weights1111[i])
            weights11111[i] = int(weights11111[i])
            weights111111[i] = int(weights111111[i])
            weights1111111[i] = int(weights1111111[i])
            biashidden1[i] = int(biashidden1[i])
            weights2[i] = int(weights2[i])
            weights22[i] = int(weights22[i])
            weights222[i] = int(weights222[i])
            weights2222[i] = int(weights2222[i])
            weights22222[i] = int(weights22222[i])
            weights222222[i] = int(weights222222[i])
            weights2222222[i] = int(weights2222222[i])
            biasoutput[i] = int(biasoutput[i])

        def neuralnetwork(inputarray, weights1, weights11, weights111, weights1111, weights11111, weights111111, weights1111111, biashidden1, weights2, weights22, weights222, weights2222, weights22222, weights222222, weights2222222):
            hiddenneuron = []
            hiddenneuron.append(sigmoid(inputarray[0]*weights1[0]+inputarray[1]*weights11[0]+inputarray[2]*weights111[0]+inputarray[3] *
                                        weights1111[0]+inputarray[4]*weights11111[0]+inputarray[5]*weights111111[0]+inputarray[6]*weights1111111[0]+biashidden1[0]))
            hiddenneuron.append(sigmoid(inputarray[0]*weights1[1]+inputarray[1]*weights11[1]+inputarray[2]*weights111[1]+inputarray[3] *
                                        weights1111[1]+inputarray[4]*weights11111[1]+inputarray[5]*weights111111[1]+inputarray[6]*weights1111111[1]+biashidden1[1]))
            hiddenneuron.append(sigmoid(inputarray[0]*weights1[2]+inputarray[1]*weights11[2]+inputarray[2]*weights111[2]+inputarray[3] *
                                        weights1111[2]+inputarray[4]*weights11111[2]+inputarray[5]*weights111111[2]+inputarray[6]*weights1111111[2]+biashidden1[2]))
            hiddenneuron.append(sigmoid(inputarray[0]*weights1[3]+inputarray[1]*weights11[3]+inputarray[2]*weights111[3]+inputarray[3] *
                                        weights1111[3]+inputarray[4]*weights11111[3]+inputarray[5]*weights111111[3]+inputarray[6]*weights1111111[3]+biashidden1[3]))
            hiddenneuron.append(sigmoid(inputarray[0]*weights1[4]+inputarray[1]*weights11[4]+inputarray[2]*weights111[4]+inputarray[3] *
                                        weights1111[4]+inputarray[4]*weights11111[4]+inputarray[5]*weights111111[4]+inputarray[6]*weights1111111[4]+biashidden1[4]))
            hiddenneuron.append(sigmoid(inputarray[0]*weights1[5]+inputarray[1]*weights11[5]+inputarray[2]*weights111[5]+inputarray[3] *
                                        weights1111[5]+inputarray[4]*weights11111[5]+inputarray[5]*weights111111[5]+inputarray[6]*weights1111111[5]+biashidden1[5]))
            hiddenneuron.append(sigmoid(inputarray[0]*weights1[5]+inputarray[1]*weights11[5]+inputarray[2]*weights111[5]+inputarray[3]*weights1111[5] +
                                        inputarray[4]*weights11111[5]+inputarray[5]*weights111111[5]+inputarray[6]*weights1111111[6]+biashidden1[6]))  # 7 total
            outputneuron = []
            outputneuron.append(sigmoid(hiddenneuron[0]*weights2[0]+hiddenneuron[1]*weights22[0]+hiddenneuron[2]*weights222[0]+hiddenneuron[3]
                                        * weights2222[0]+hiddenneuron[4]*weights22222[0]+hiddenneuron[5]*weights222222[0]+hiddenneuron[6]*weights2222222[0]+biasoutput[0]))
            outputneuron.append(sigmoid(hiddenneuron[0]*weights2[1]+hiddenneuron[1]*weights22[1]+hiddenneuron[2]*weights222[1]+hiddenneuron[3]
                                        * weights2222[1]+hiddenneuron[4]*weights22222[1]+hiddenneuron[5]*weights222222[1]+hiddenneuron[6]*weights2222222[1]+biasoutput[1]))
            outputneuron.append(sigmoid(hiddenneuron[0]*weights2[2]+hiddenneuron[1]*weights22[2]+hiddenneuron[2]*weights222[2]+hiddenneuron[3]
                                        * weights2222[2]+hiddenneuron[4]*weights22222[2]+hiddenneuron[5]*weights222222[2]+hiddenneuron[6]*weights2222222[2]+biasoutput[2]))
            outputneuron.append(sigmoid(hiddenneuron[0]*weights2[3]+hiddenneuron[1]*weights22[3]+hiddenneuron[2]*weights222[3]+hiddenneuron[3]
                                        * weights2222[3]+hiddenneuron[4]*weights22222[3]+hiddenneuron[5]*weights222222[3]+hiddenneuron[6]*weights2222222[3]+biasoutput[3]))
            if max(outputneuron[0], outputneuron[1], outputneuron[2], outputneuron[3]) == outputneuron[0]:
                return 0
            if max(outputneuron[0], outputneuron[1], outputneuron[2], outputneuron[3]) == outputneuron[1]:
                return 1
            if max(outputneuron[0], outputneuron[1], outputneuron[2], outputneuron[3]) == outputneuron[2]:
                return 2
            if max(outputneuron[0], outputneuron[1], outputneuron[2], outputneuron[3]) == outputneuron[3]:
                return 3

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
                timealive = runtime-begintime
                if timealive > 10:
                    doexit = True
                fitness = timealive/float(fps)+score*10
                #print("your fitness is: %s")%fitness
                headnewposarray = [snakearray[0][0] +
                                   amt_to_add(direction, 'x'), snakearray[0][1] + amt_to_add(direction, 'y')]
                snakearray.insert(0, headnewposarray)  # add new first element to the array
                del snakearray[len(snakearray)-1]  # delete the last element on that array
                if snakearray[0][0] == 40 or snakearray[0][1] == 40 or snakearray[0][0] == -1 or snakearray[0][1] == -1:
                    print "YOU LOST"
                    doexit = True
                for i in range(len(snakearray)-1):
                    if snakearray[0][0] == snakearray[i+1][0] and snakearray[0][1] == snakearray[i+1][1]:
                        print "YOU LOST!"
                        doexit = True
                drawing_pixel(snakearray, 'black')
                drawing_pixel(food, 'red')
                update()

                if snakearray[0][0] == food[0] and snakearray[0][1] == food[1]:  # check if the food has been eaten
                    food = rand_food_pos()
                    score = score + 10
                    # add the latest element to the snake's body (tail)
                    snakearray.append(snakearray[len(snakearray)-1])
                # calculate the distance from wall/body
                for i in range(len(snakearray)-1):  # First find the closest distance from the body to the snake
                    # if the body is to the snake's right, when we subtract the head's x coord from the body x's coord we should get a negative number.
                    if snakearray[0][0] - snakearray[i+1][0] < 0:
                        # check if the distance between head and tail is smaller than the one we already have
                        if abs(snakearray[0][0] - snakearray[i+1][0]) < closestright:
                            # update the value of closest element to the right of the snake. Also make the value positive
                            closestright = abs(snakearray[0][0] - snakearray[i+1][0])
                    # repeat for x to the left and for y in both directions.
                    if snakearray[0][0] - snakearray[i+1][0] > 0:
                        if snakearray[0][0] - snakearray[i+1][0] < closestleft:
                            # taking the abs value is optional
                            closestleft = abs(snakearray[0][0] - snakearray[i+1][0])
                    if snakearray[0][1] - snakearray[i+1][1] > 0:  # if above, head pos - tail pos is positive
                        if snakearray[0][1] - snakearray[i+1][1] < closestup:
                            # taking the abs value is optional
                            closestup = abs(snakearray[0][1] - snakearray[i+1][1])
                    if snakearray[0][1] - snakearray[i+1][1] < 0:  # if below, head pos - tail pos is negative
                        if abs(snakearray[0][1] - snakearray[i+1][1]) < closestdown:
                            # taking the abs value is optional
                            closestdown = abs(snakearray[0][1] - snakearray[i+1][1])
                # DIVIDE ALL VALUES BY 40 THEN PASS THROUGH SIGMOID
                if snakearray[0][0] < closestleft:  # Leftwall
                    closestleft = (snakearray[0][0])/float(40)
                if abs(snakearray[0][0] - 40) < closestright:
                    closestright = (abs(snakearray[0][0] - 40))/float(40)
                if snakearray[0][1] < closestup:
                    closestup = (20-snakearray[0][1])/float(40)
                if abs(snakearray[0][1] - 40) < closestdown:
                    closestdown = (abs(snakearray[0][1] - 40))/float(40)
                inputarray = [direction, closestup, closestdown,
                              closestleft, closestright, applex, appley]

                for i in range(len(inputarray)):
                    if i == 0:
                        inputarray[i] = sigmoid(inputarray[i])
                applex = calcappledist(food[0], snakearray[0][0])
                appley = calcappledist(food[1], snakearray[0][1])

                neuraldirection = neuralnetwork(inputarray, weights1, weights11, weights111, weights1111, weights11111, weights111111,
                                                weights1111111, biashidden1, weights2, weights22, weights222, weights2222, weights22222, weights222222, weights2222222)
                direction = checkdirection(direction, neuraldirection)
                closestup = 40  # Reset the values
                closestright = 40
                closestdown = 40
                closestleft = 40

                k = win.checkKey()  # register the last key that was pressed
                if k == "e":
                    doexit = True  # Click e to exit!
                #direction = check_key(k, direction)

        win.close()

        afitness.write(str(fitness))
        afitness.close()
        avg_fitness = avg_fitness + fitness
    print avg_fitness
    print avg_fitness/100


runsnakegamextimes(100)
