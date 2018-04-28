# This is a Snake game by Henrijs and Luca, using the
# standard graphics.py library !
# 28 april 2018

###IMPORTS###
from graphics import *
import time
from random import randint
from function_Snake_Game import *


# ###FUNCTIONS###
def rand_pos():
    return [randint(0, size_of_win-1), randint(0, size_of_win-1)]


# draws either one set of position or an array of position
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
